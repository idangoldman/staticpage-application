from bs4 import BeautifulSoup
from flask import current_app
from shutil import copyfile, make_archive
import re

from backend.helpers import path_builder
from backend.helpers.folder_maker import user_folder_uri


def zip_a_page( page_content, dest_path, file_name ):
    user_folder_path = path_builder( current_app.config['BASE_PATH'], \
                                     current_app.config['USER_FOLDER'] )
    soup = BeautifulSoup( page_content, 'html5lib' )

    file_paths = []
    img_tags = soup.find_all('img')
    link_tags = soup.find_all('link', { 'class', 'css-page' })
    styles_tag = soup.find_all('style', { 'class', 'css-intervention' })


    for img in img_tags:
        original_path = img.get('src')
        new_path = 'images/' + original_path.split('/')[ -1 ]

        img['src'] = new_path

        file_paths.append({
            'original': path_builder( user_folder_path, original_path ),
            'new': path_builder( dest_path, new_path )
        })


    for link in link_tags:
        original_path = link.get('href')
        new_path = 'css/' + original_path.split('/')[ -1 ]

        link['href'] = new_path
        file_paths.append({
            'original': path_builder( current_app.config['BASE_PATH'], original_path ),
            'new': path_builder( dest_path, new_path )
        })


    for style in styles_tag:
        background_images = re.findall( r"(?:\(['\"]?)(\/uploads\/.*?)(?:['\"]?\))", style.text );

        for background_image in background_images:
            original_path = background_image
            new_path = 'images/' + original_path.split('/')[-1]

            style.string = style.text.replace( original_path, new_path )

            file_paths.append({
                'original': path_builder( user_folder_path, original_path ),
                'new': path_builder( dest_path, new_path )
            })


    for path in file_paths:
        copyfile( path['original'], path['new'] )


    with open( dest_path + '/index.html', 'w' ) as file:
        encoded_html = soup.encode('utf-8')
        filtered_html = filter( lambda line_of_code: line_of_code.strip(), encoded_html.split('\n') )
        html = '\n'.join( filtered_html )

        file.write( html )

    file_path = make_archive( dest_path + '/' + file_name, 'zip',  dest_path )


    file_uri = user_folder_uri( file_path )
    return file_uri
