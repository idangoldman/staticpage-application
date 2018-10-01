from flask import render_template, current_app, json, send_from_directory, make_response, request, redirect, url_for, flash
from flask_login import login_required, current_user

from backend.helpers import path_builder, is_phone, get_page_stub
from backend.models.page import Page
from backend.models.user import User
from backend.third_party import mailchimp_subscribe
from backend.website.forms import NewsletterForm


@current_app.route('/')
def index_route():
    if current_user.is_authenticated:
        return redirect( url_for('home') )
    else:
        return redirect( url_for('website.welcome') )


@current_app.route( '/page_intervention/<int:page_id>', methods=['GET', 'POST'] )
@login_required
def page_intervention( page_id ):
    payload = current_user.pages.first().with_defaults()
    payload['is_intervention'] = True

    form = NewsletterForm()

    if form.validate_on_submit():
        has_subscribed = mailchimp_subscribe(
            form.email.data,
            payload['mailing_list_mailchimp_username'],
            payload['mailing_list_mailchimp_api_key'],
            payload['mailing_list_mailchimp_list_id']
        )

        if has_subscribed:
            if payload.get('mailing_list_successful_submission') == 'successful-submission-message' \
                and payload.get('mailing_list_message'):
                flash( payload.get('mailing_list_message') )
            elif payload.get('mailing_list_successful_submission') == 'successful-submission-redirect' \
                and payload.get('mailing_list_redirect_url'):
                return redirect( payload.get('mailing_list_redirect_url') )

    return render_template( 'page/index.html', **payload )


@current_app.route('/page/<site_name>')
def page_view( site_name ):
    payload = Page.query.join( Page.creator ) \
                     .filter( User.site_name == site_name ) \
                     .first_or_404() \
                     .with_defaults()


    form = NewsletterForm()

    if form.validate_on_submit():
        has_subscribed = mailchimp_subscribe(
            form.email.data,
            payload['mailing_list_mailchimp_username'],
            payload['mailing_list_mailchimp_api_key'],
            payload['mailing_list_mailchimp_list_id']
        )

        if has_subscribed:
            if payload.get('mailing_list_successful_submission') == 'successful-submission-message' \
                and payload.get('mailing_list_message'):
                flash( payload.get('mailing_list_message') )
            elif payload.get('mailing_list_successful_submission') == 'successful-submission-redirect' \
                and payload.get('mailing_list_redirect_url'):
                return redirect( payload.get('mailing_list_redirect_url') )


    return render_template( 'page/index.html', **payload )


@current_app.route('/home')
@login_required
def home():
    payload = {
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'on_phone': is_phone( request.user_agent ),
        'page_id': current_user.pages.first().id,
        'site_name': current_user.site_name
    }

    response = make_response( render_template( 'home.html', **payload ) )
    if not request.cookies.get('show_login_link'):
        response.set_cookie( 'show_login_link', value='1', max_age=30585600 ) #one year expiration

    return response


@current_app.route('/side-kick/<int:page_id>')
@login_required
def side_kick( page_id ):
    with open( 'static/images/side-kick-sprite.svg', 'r' ) as svg_file:
        svg_sprite = svg_file.read()
    with open( 'backend/stubs/features.json', 'r' ) as json_file:
        features = json.load( json_file )

    page_with_features = current_user.pages.first().with_features()

    payload = {
        'features': page_with_features,
        'blog_url': current_app.config['BLOG_URL'],
        'is_email_confirmed': current_user.email_confirmed,
        'on_phone': is_phone( request.user_agent ),
        'page_update_url': current_app.config['API_URL'] + '/page/update/' + str( page_id ),
        'site_download_url': current_app.config['API_URL'] + '/download/' + current_user.site_name,
        'page_id': page_id,
        'site_name': current_user.site_name,
        'svg_sprite': svg_sprite,
        'user_id': current_user.id
    }

    return render_template( 'side-kick/index.html', **payload )


@current_app.route('/<user_hash>/uploads/<timestamp>/<file_name>')
def user_uploads( user_hash, timestamp, file_name ):
    upload_folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['TMP_FOLDER'], \
                                user_hash, \
                                'uploads', \
                                timestamp )
    return send_from_directory( upload_folder_path, file_name )


@current_app.route('/<hash>/<timestamp>/<file_name>')
def user_downloads( hash, timestamp, file_name ):
    donwload_folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['TMP_FOLDER'], \
                                hash, \
                                '/', \
                                timestamp )
    return send_from_directory( donwload_folder_path, file_name )


@current_app.errorhandler(401)
def page_unauthorized(e):
    return render_template('website/_base.html', \
                            page=get_page_stub('errors/500')), 401


@current_app.errorhandler(403)
def page_forbidden(e):
    return render_template('website/_base.html', \
                            page=get_page_stub('errors/500')), 403


@current_app.errorhandler(404)
def page_not_found(e):
    return render_template('website/_base.html', \
                            page=get_page_stub('errors/404')), 404


@current_app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('website/_base.html', \
                            page=get_page_stub('errors/500')), 500


@current_app.errorhandler(503)
def page_service_unavailable(e):
    return render_template('website/_base.html', \
                            page=get_page_stub('errors/500')), 503
