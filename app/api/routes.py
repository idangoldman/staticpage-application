from flask import current_app, request, jsonify, escape, g

from . import api, errors
from app.helpers import path_builder
from app.helpers.upload_file import upload_file
from app.helpers.folder_maker import user_folder_path
from app import db
from app.models import Page


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
        request_data['value'] = escape( request_data['value'] )
        setattr( page, request_data['name'], request_data['value'] )
        db.session.commit()

        response_data = request_data

    return jsonify( { 'status': 'ok', 'data': response_data } )

# @api.before_request
# def before_api_request():
#     if request.json is None:
#         return errors.bad_request('Invalid JSON in body.')
#     token = request.json.get('token')
#     if not token:
#         return errors.unauthorized('Authentication token not provided.')
#     user = User.validate_api_token(token)
#     if not user:
#         return errors.unauthorized('Invalid authentication token.')
#     g.current_user = user
