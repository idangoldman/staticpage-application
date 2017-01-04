from flask import render_template, current_app, redirect, make_response, json, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from app.third_party import mailchimp_subscribe


class NewsletterForm(FlaskForm):
    email = StringField("email", [validators.Required(), validators.Email("Please enter your email address.")])


@current_app.route('/')
def index_route():
    return redirect('/welcome')


@current_app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form = NewsletterForm(request.form)

    if request.method == 'POST' and form.validate():
        if mailchimp_subscribe(form.email.data):
            return redirect('/thank-you')

    with open('app/stubs/features.json', 'r') as json_file:
        features = json.load( json_file )
    with open('app/stubs/welcome_page.json', 'r') as json_file:
        page_stub = json.load( json_file )

    for feature in features:
        for field in feature.get('fields'):
            if not page_stub.get( field.get('id') ) and field.get('default'):
                page_stub[ field.get('id') ] = field.get('default')

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'pub_id': current_app.config['ADDTHIS_PUBID'],
        'has_subscribed': request.cookies.get('has_subscribed'),
        'page': page_stub,
    }

    return render_template('website/welcome.html', **payload)


@current_app.route('/thank-you')
def thank_you():
    payload = {
        'pub_id': current_app.config['ADDTHIS_PUBID'],
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID']
    }

    response = make_response(render_template('website/thank-you.html', **payload))
    response.set_cookie('has_subscribed', 'true')
    return response


@current_app.errorhandler(401)
def page_unauthorized(e):
    return render_template('website/errors/401.html'), 401


@current_app.errorhandler(403)
def page_forbidden(e):
    return render_template('website/errors/403.html'), 403


@current_app.errorhandler(404)
def page_not_found(e):
    return render_template('website/errors/404.html'), 404


@current_app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('website/errors/500.html'), 500


@current_app.errorhandler(503)
def page_service_unavailable(e):
    return render_template('website/errors/503.html'), 503
