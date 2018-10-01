from bs4 import BeautifulSoup
from flask import current_app, render_template
from shutil import copyfile, make_archive, rmtree
import re
import os
import requests
import boto3

from backend.helpers import path_builder


def zip_a_page( markup, dest_path, page ):
    archive_name = path_builder( dest_path, page.get('file_name') )
    archive_root = path_builder( dest_path, 'page' )
    index_file_extention = 'html'

    soup = BeautifulSoup( markup, 'html5lib' )

    file_paths = []
    img_tags = soup.find_all('img')
    link_tags = soup.find_all('link', { 'class', 'css-page' })
    style_tags = soup.find_all('style', { 'class', 'css-intervention' })
    mailing_list = soup.find('form', { 'class', 'newsletter' })

    for img in img_tags:
        original_path = img.get('src')
        new_path = 'images/' + original_path.split('/')[ -1 ]

        img['src'] = new_path

        file_paths.append({
            'original': original_path,
            'new': path_builder( archive_root, new_path )
        })


    for link in link_tags:
        original_path = link.get('href')
        new_path = 'css/' + original_path.split('/')[ -1 ]

        link['href'] = new_path
        file_paths.append({
            'original': path_builder( current_app.config['BASE_PATH'], original_path ),
            'new': path_builder( archive_root, new_path )
        })


    for style in style_tags:
        background_images = re.findall( r"background-image: url(?:\(['\"]?)(.*?)(?:['\"]?\))", style.text );

        for background_image in background_images:
            original_path = background_image
            new_path = 'images/' + original_path.split('/')[-1]

            style.string = style.text.replace( original_path, new_path )

            file_paths.append({
                'original': original_path,
                'new': path_builder( archive_root, new_path )
            })


    if mailing_list:
        index_file_extention = 'php'
        soup.insert(0, "<?php require_once( './mailing-list.php' ); ?>")
        mailing_list.find('div')['style'] = '<?php hide_form(); ?>'
        mailing_list.select('input[name="csrf_token"]')[0]['value'] = '<?php csrf_token(); ?>'
        mailing_list.append('<?php print_message(); ?>')

        file_paths.append({
            'original': 'third-party/mailchimp.php',
            'new': path_builder( archive_root, 'mailing-list.php' ),
            'data': {
                'api_key': page.get('mailing_list_mailchimp_api_key'),
                'list_id': page.get('mailing_list_mailchimp_list_id'),
                'username': page.get('mailing_list_mailchimp_username'),
                'successful_submission': page.get('mailing_list_successful_submission'),
                'redirect_url': page.get('mailing_list_redirect_url'),
                'message': page.get('mailing_list_message')
            }
        })


    for path in file_paths:
        if path.get('data'):
            template = render_template( path.get('original'), **path.get('data') )

            with open( path.get('new'), 'wb' ) as file:
                file.write( template )

        elif 'https://' in path.get('original'):
            raw_file = requests.get( path.get('original'), timeout = 10, verify = False ).content;

            with open( path.get('new'), 'w' ) as file:
                file.write( raw_file )
        else:
            copyfile( path.get('original'), path.get('new') )


    with open( archive_root + '/index.' + index_file_extention, 'w' ) as file:
        encoded_file = soup.encode(formatter=None)
        filtered_file = filter( lambda line_of_code: line_of_code.strip(), encoded_file.split('\n') )
        output = '\n'.join( filtered_file )

        file.write( output )

    archived_file_path = make_archive( archive_name, 'zip', archive_root )
    bucket_archived_file_path = archived_file_path.rsplit( 'tmp/', 1 )[ 1 ].lower()

    try:
        boto3.client('s3').upload_file(
            archived_file_path,
            os.environ['AWS_S3_BUCKET'],
            bucket_archived_file_path,
            {
                'ACL': 'public-read',
                'ContentType': 'zip'
            }
        )
    except Exception as e:
        return None

    rmtree(dest_path[:dest_path.rfind('/')], ignore_errors=True)

    return "{}{}".format(current_app.config['AWS_S3_BUCKET_URL'], bucket_archived_file_path)
