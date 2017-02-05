from bs4 import BeautifulSoup
from flask import current_app, request, jsonify, escape, g
from shutil import copyfile, make_archive
import requests, re

from backend import db
from backend.api import api, errors
from backend.helpers import path_builder
from backend.helpers.folder_maker import create_uploads_folder
from backend.helpers.upload_file import upload_file
from backend.models.page import Page


@api.route('/download/<site_name>', methods=['GET'])
def download(site_name):
    page = requests.get( 'http://127.0.0.1:5000/page/' + site_name, timeout = 1 );
    soup = BeautifulSoup(page.content, 'html5lib')

    file_paths = []
    img_tags = soup.find_all('img')
    link_tags = soup.find_all('link', { 'class', 'css-page' })
    styles_tag = soup.find_all('style', { 'class', 'css-intervention' })

    for img in img_tags:
        original_path = img.get('src')
        new_path = 'images/' + original_path.split('/')[-1]

        img['src'] = new_path

        file_paths.append({
            'original': original_path,
            'new': new_path
        })

    for link in link_tags:
        original_path = link.get('href')
        new_path = 'css/' + original_path.split('/')[-1]

        link['href'] = new_path

        file_paths.append({
            'original': original_path,
            'new': new_path
        })

    for style in styles_tag:
        background_images = re.findall(r"(?:\(['\"]?)(\/uploads\/.*?)(?:['\"]?\))", style.text);

        for background_image in background_images:
            original_path = background_image
            new_path = 'images/' + original_path.split('/')[-1]

            style.string = style.text.replace( original_path, new_path )

            file_paths.append({
                'original': original_path,
                'new': new_path
            })

    for path in file_paths:
        copyfile( current_app.config['BASE_PATH'] + path['original'], current_app.config['BASE_PATH'] + '/user_data/' + path['new'] )

    with open( current_app.config['BASE_PATH'] + '/user_data/index.html', 'w' ) as file:
        # encoded_html = soup.prettify( formatter = "html" ).encode('utf-8')
        encoded_html = soup.encode('utf-8')
        filtered_html = filter( lambda line_of_code: line_of_code.strip(), encoded_html.split('\n') )
        html = '\n'.join( filtered_html )

        file.write( html )

    make_archive( current_app.config['BASE_PATH'] + '/' + site_name + '_website', 'zip',  current_app.config['BASE_PATH'] + '/user_data/' )

    payload = {
        'url': '/uploads/blah_website.zip'
    }

    return jsonify( { 'status': 'ok', 'data': payload } )


@api.route('/page/update/<int:id>', methods=['POST'])
def page(id):
    page = Page.query.get_or_404(id)

    if request.files:
        creator_email = page.creator.email
        upload_folder_path = create_uploads_folder( creator_email )

        for field_name in request.files:
            upload_file_uri = upload_file( request.files[ field_name ], upload_folder_path )

        if not upload_file_uri:
            return errors.bad_request('file was not uploaded')

        setattr( page, field_name, upload_file_uri )
        db.session.commit()

        response_data = {
            'name': field_name,
            'value': upload_file_uri
        }

    else:
        request_data = request.get_json()
        setattr( page, request_data['name'], request_data['value'] )
        db.session.commit()

        response_data = request_data

    return jsonify( { 'status': 'ok', 'data': response_data } )
