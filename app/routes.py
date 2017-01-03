from flask import render_template, current_app, redirect, make_response, json, request, jsonify, send_from_directory
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from flask_wtf.csrf import CsrfProtect
from wtforms import StringField, validators

from app.third_party import mailchimp_subscribe
from app.helpers import path_builder


class NewsletterForm(FlaskForm):
    email = StringField("email", [validators.Required(), validators.Email("Please enter your email address.")])

@current_app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form = NewsletterForm(request.form)

    if request.method == 'POST' and form.validate():
        if mailchimp_subscribe(form.email.data):
            return redirect('/thank-you')

    with open('app/stubs/features.json', 'r') as json_file:
        features = json.load( json_file )
    with open('app/stubs/user_page.json', 'r') as json_file:
        user_page = json.load( json_file )

    for feature in features:
        if feature['name'] in user_page:
            for field in feature['fields']:
                if field['name'] in user_page[feature['name']]:
                    if not user_page[feature['name']][field['name']] and 'default' in field:
                        user_page[feature['name']][field['name']] = field['default']

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'pub_id': current_app.config['ADDTHIS_PUBID'],
        'has_subscribed': request.cookies.get('has_subscribed'),
        'content': user_page['content'],
        'design': user_page['design']
    }

    return render_template('pages/welcome.html', **payload)


@current_app.route('/thank-you')
def thank_you():
    payload = {
        'pub_id': current_app.config['ADDTHIS_PUBID'],
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID']
    }

    response = make_response(render_template('pages/thank-you.html', **payload))
    response.set_cookie('has_subscribed', 'true')
    return response


@current_app.route('/')
@current_app.route('/pages')
def index_route():
    return redirect('/welcome')


@current_app.route('/page_intervention/<int:page_id>')
@login_required
def page_intervention(page_id):
    payload = current_user.pages.first().__dict__
    payload['is_intervention'] = True

    return render_template('pages/layout.html', **payload)


@current_app.route('/home')
@login_required
def home():
    payload = {
        'site_name': current_user.site_name,
        'page_id': current_user.pages.first().id
    }
    return render_template('pages/home.html', **payload)


@current_app.route('/side-kick/<int:page_id>')
@login_required
def side_kick(page_id):
    with open('static/images/side-kick-sprite.svg', 'r') as svg_file:
        svg_sprite = svg_file.read()
    with open('app/stubs/features.json', 'r') as json_file:
        features = json.load( json_file )

    page = current_user.pages.first().__dict__

    for feature in features:
        for field in feature['fields']:
            if field.has_key('id') and page[field['id']]:
                field['value'] = page[field['id']]

    payload = {
        'svg_sprite': svg_sprite,
        'features': features,
        'page_api_url': current_app.config['API_URL'] + '/page/' + str(page_id),
    }

    return render_template('pages/side-kick.html', **payload)

@current_app.route('/flex-color')
def flex_color():
    return render_template('pages/flex-color.html')


@current_app.route('/uploads/<user_hash>/<file_name>')
def user_uploads( user_hash, file_name ):
    upload_folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['UPLOAD_FOLDER'], \
                                user_hash )
    return send_from_directory( upload_folder_path, file_name )


@current_app.errorhandler(401)
def page_unauthorized(e):
    return render_template('pages/errors/401.html'), 401


@current_app.errorhandler(403)
def page_forbidden(e):
    return render_template('pages/errors/403.html'), 403


@current_app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/errors/404.html'), 404


@current_app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('pages/errors/500.html'), 500


@current_app.errorhandler(503)
def page_service_unavailable(e):
    return render_template('pages/errors/503.html'), 503
