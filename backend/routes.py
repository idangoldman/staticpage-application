from flask import render_template, current_app, json, send_from_directory, make_response, request, redirect, url_for, flash
from flask_login import login_required, current_user

from backend.helpers import path_builder, get_page_stub, get_a_stub
from backend.models.page import Page
from backend.models.user import User
from backend.third_party import mailchimp_subscribe
from backend.auth.forms import NewsletterForm


@current_app.route('/')
def index_route():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        payload = {
            'page': get_page_stub('website'),
            'mailchimp_details': {
              "list_id": current_app.config['MAILCHIMP_LIST_ID'],
              "user_id": current_app.config['MAILCHIMP_USER_ID'],
              "url": current_app.config['MAILCHIMP_FORM_URL'],
              "antispam_field_name": current_app.config['MAILCHIMP_ANTISPAM_FIELD_NAME']
            }
        }

        return render_template('website.html', **payload)

@current_app.route('/welcome')
def welcome_route():
    return redirect('/')


@current_app.route('/page_intervention/<int:page_id>', methods=['GET', 'POST'])
@login_required
def page_intervention(page_id):
    payload = current_user.pages.filter_by(id=page_id).first_or_404().with_defaults()
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
                flash(payload.get('mailing_list_message'))
            elif payload.get('mailing_list_successful_submission') == 'successful-submission-redirect' \
                and payload.get('mailing_list_redirect_url'):
                return redirect(payload.get('mailing_list_redirect_url'))

    return render_template('page/index.html', **payload)


@current_app.route('/preview/<site_name>/<page_name>')
@login_required
def page_preview(site_name, page_name):
    payload = Page.query.join(Page.creator) \
                     .filter(User.site_name == site_name, Page.name == page_name) \
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
                return redirect(payload.get('mailing_list_redirect_url'))


    return render_template( 'page/index.html', **payload )

@current_app.route('/preview-download/<site_name>/<page_name>')
def page_preview_download(site_name, page_name):
    payload = Page.query.join(Page.creator) \
                     .filter(User.site_name == site_name, Page.name == page_name) \
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
                return redirect(payload.get('mailing_list_redirect_url'))


    return render_template( 'page/index.html', **payload )


@current_app.route('/home/', defaults={'site_name': None, 'page_name': None})
@current_app.route('/home/<site_name>/<page_name>')
@login_required
def home(site_name, page_name):
    if site_name is not None and page_name is not None:
      page = current_user.pages.filter_by(name=page_name).first_or_404()
    else:
      page = current_user.pages.first()

    payload = {
        'page_id': page.id,
        'site_name': current_user.site_name,
        'title': page.content_title
    }

    return make_response(render_template('home.html', **payload))


@current_app.route('/side-kick/<int:page_id>')
@login_required
def side_kick(page_id):
    with open('static/images/side-kick-sprite.svg', 'r') as svg_file:
        svg_sprite = svg_file.read()

    features = get_a_stub('features/all')
    page_with_features = current_user.pages.filter_by(id=page_id).first_or_404().with_features()


    manage_pages = get_a_stub('features/manage-pages')
    pages = current_user.pages.with_entities(Page.id, Page.name).all();
    for field in manage_pages.get('fields'):
      if field.get('id') == 'manage_pages_pages':
        for page in pages:
          page_url = '/home/' + current_user.site_name + '/' + page[1]
          field['options'].append({'key': page_url, 'value': page[1]})

          if page[0] == page_id:
            field['default'] = page_url

      if field.get('id') == 'manage_pages_actions':
        field['id'] = field.get('id') + '_' + str(page_id)

    payload = {
        'manage_pages': manage_pages,
        'features': page_with_features.get('features'),
        'is_email_confirmed': current_user.email_confirmed,
        'page_update_url': current_app.config['API_URL'] + '/page/update/' + str(page_id),
        'site_download_url': current_app.config['API_URL'] + '/download/' + current_user.site_name + '/' + page_with_features.get('page').get('name'),
        'page_manage_url': current_app.config['API_URL'] + '/page_manage/' + current_user.site_name,
        'page_id': page_id,
        'page_name': page_with_features.get('page').get('name'),
        'site_name': current_user.site_name,
        'svg_sprite': svg_sprite,
        'user_id': current_user.id
    }

    return render_template('side-kick/index.html', **payload)

@current_app.route('/side-kick/new-page/')
@login_required
def side_kick_new_page():
    with open('static/images/side-kick-sprite.svg', 'r') as svg_file:
        svg_sprite = svg_file.read()

    new_page = get_a_stub('features/new-page')

    payload = {
        'svg_sprite': svg_sprite,
        'page': new_page,
        'is_email_confirmed': current_user.email_confirmed,
        'page_manage_url': current_app.config['API_URL'] + '/page_manage/' + current_user.site_name,
    }

    return render_template('side-kick/new-page.html', **payload)


@current_app.errorhandler(401)
def page_unauthorized(e):
    return render_template('errors.html', \
                            page=get_page_stub('errors/500')), 401


@current_app.errorhandler(403)
def page_forbidden(e):
    return render_template('errors.html', \
                            page=get_page_stub('errors/500')), 403


@current_app.errorhandler(404)
def page_not_found(e):
    return render_template('errors.html', \
                            page=get_page_stub('errors/404')), 404


@current_app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('errors.html', \
                            page=get_page_stub('errors/500')), 500


@current_app.errorhandler(503)
def page_service_unavailable(e):
    return render_template('errors.html', \
                            page=get_page_stub('errors/500')), 503
