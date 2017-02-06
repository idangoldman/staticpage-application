from flask import current_app, request, jsonify
import requests

from backend import db
from backend.api import api, errors
from backend.helpers import path_builder
from backend.helpers.folder_maker import create_uploads_folder, create_download_folder
from backend.helpers.upload_file import upload_file
from backend.helpers.download_file import zip_a_page
from backend.models.page import Page
from backend.models.user import User


@api.route('/download/<site_name>', methods=['GET'])
def download(site_name):
    user = User.query.filter( site_name == site_name ).first_or_404()

    try:
        page = requests.get( current_app.config['HTTP_HOST'] + '/page/' + site_name, timeout = 10 );
    except requests.exceptions.RequestException as e:
        return errors.bad_request('page can\'t be reached')

    download_folder_path = create_download_folder( user.email )
    zip_uri = zip_a_page( page.content, download_folder_path, site_name + '_page' )

    payload = {
        'url': current_app.config['HTTP_HOST'] + zip_uri
    }

    return jsonify( { 'status': 'ok', 'data': payload } )


@api.route('/page/update/<int:id>', methods=['POST'])
def page( id ):
    page = Page.query.get_or_404( id )

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
