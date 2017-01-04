from flask import render_template, current_app, json, jsonify, send_from_directory
from flask_login import login_required, current_user

from app.helpers import path_builder
from app.models.user import User
from app.models.page import Page


@current_app.route('/page_intervention/<int:page_id>')
@login_required
def page_intervention(page_id):
    payload = current_user.pages.first().with_defaults()
    payload['is_intervention'] = True

    return render_template('page/index.html', **payload)


@current_app.route('/page/<site_name>')
def page_view( site_name ):
    payload = Page.query.join( Page.creator ) \
                     .filter( User.site_name == site_name ) \
                     .first_or_404() \
                     .with_defaults()

    return render_template( 'page/index.html', **payload )


@current_app.route('/home')
@login_required
def home():
    payload = {
        'site_name': current_user.site_name,
        'page_id': current_user.pages.first().id
    }
    return render_template( 'home.html', **payload )


@current_app.route('/side-kick/<int:page_id>')
@login_required
def side_kick(page_id):
    with open('static/images/side-kick-sprite.svg', 'r') as svg_file:
        svg_sprite = svg_file.read()
    with open('app/stubs/features.json', 'r') as json_file:
        features = json.load( json_file )

    page_with_features = current_user.pages.first().with_features()

    payload = {
        'svg_sprite': svg_sprite,
        'features': page_with_features,
        'site_name': current_user.site_name,
        'page_api_url': current_app.config['API_URL'] + '/page/' + str(page_id),
    }

    return render_template( 'side-kick.html', **payload )


@current_app.route('/uploads/<user_hash>/<timestamp>/<file_name>')
def user_uploads( user_hash, timestamp, file_name ):
    upload_folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['UPLOAD_FOLDER'], \
                                user_hash, \
                                timestamp )
    return send_from_directory( upload_folder_path, file_name )
