from flask import current_app, request, jsonify, escape, g

from backend import db
from backend.api import api, errors
from backend.helpers import path_builder
from backend.helpers.folder_maker import user_folder_path
from backend.helpers.upload_file import upload_file
from backend.models.page import Page

@api.route('/page/download/<int:id>', methods=['POST'])
def download(id):
    return jsonify( { 'status': 'ok', 'data': request.get_json() } )

@api.route('/page/<int:id>', methods=['POST'])
def page(id):
    # if page.creator != g.current_user \
    #         and not g.current_user.is_admin:
    #     return errors.unauthorized

    page = Page.query.get_or_404(id)

    if request.files:
        creator_email = page.creator.email
        upload_folder_path = user_folder_path( creator_email )

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
