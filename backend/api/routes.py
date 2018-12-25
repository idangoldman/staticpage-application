from datetime import datetime
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


@api.route('/download/<site_name>/<page_name>', methods=['GET'])
def download(site_name, page_name):
    try:
        page_response = requests.get( current_app.config['HTTP_HOST'] + '/preview/' + site_name + '/' + page_name, timeout = 10, verify = False );
    except requests.exceptions.RequestException as e:
        return errors.bad_request('page can\'t be reached')

    page = Page.query.join(Page.creator) \
                     .filter(User.site_name == site_name, Page.name == page_name) \
                     .first_or_404();

    page_data = page.with_defaults()
    page_data['file_name'] = page.creator.site_name + '_' + page.name
    download_folder_path = create_download_folder( page.creator.email )
    zip_uri = zip_a_page( page_response.content, download_folder_path, page_data )


    if zip_uri:
        payload = {
            'url': zip_uri
        }

        return jsonify({ 'status': 'ok', 'data': payload })
    else:
        return errors.bad_request('something happend while trying to download the file')


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

        if request_data['name'] in page.__dict__:

            if 'countdown_datetime' == request_data['name']:
                if request_data['value']:
                    request_data['value'] = datetime.strptime( request_data['value'], '%Y/%m/%d %H:%M' )
                else:
                    request_data['value'] = None

            try:
                setattr( page, request_data['name'], request_data['value'] )
                db.session.commit()
            except Exception, e:
                return errors.bad_request( 'field was not saved' )

            response_data = request_data
        else:
            return errors.bad_request('field can\'t be reached')

    return jsonify( { 'status': 'ok', 'data': response_data } )
