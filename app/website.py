from flask import render_template, current_app, redirect, make_response, json, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from app.third_party import mailchimp_subscribe


class NewsletterForm(FlaskForm):
    email = StringField("email", [validators.Required(), validators.Email("Please enter your email address.")])

def get_page_stub( name ):
    with open('app/stubs/features.json', 'r') as json_file:
        features = json.load( json_file )
    with open('app/stubs/website/' + name + '.json', 'r') as json_file:
        page_stub = json.load( json_file )

    for feature in features:
        for field in feature.get('fields'):
            if not page_stub.get( field.get('id') ):
                if field.get('default'):
                    page_stub[ field.get('id') ] = field.get('default')
                if field.get('id') == 'search_results_title':
                    page_stub['search_results_title'] = page_stub.get('content_title')
                if field.get('id') == 'search_results_description':
                    page_stub['search_results_description'] = page_stub.get('content_sub_title')

    return page_stub


@current_app.route('/')
def index_route():
    return redirect('/welcome')


@current_app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form = NewsletterForm(request.form)

    if request.method == 'POST' and form.validate():
        if mailchimp_subscribe(form.email.data):
            return redirect('/thank-you')

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'pub_id': current_app.config['ADDTHIS_PUBID'],
        'has_subscribed': request.cookies.get('has_subscribed'),
        'page': get_page_stub('welcome'),
    }

    return render_template('website/welcome.html', **payload)


@current_app.route('/thank-you')
def thank_you():
    payload = {
        'pub_id': current_app.config['ADDTHIS_PUBID'],
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'page': get_page_stub('thank_you')
    }

    response = make_response(render_template('website/thank-you.html', **payload))
    response.set_cookie('has_subscribed', 'true')
    return response


@current_app.errorhandler(401)
def page_unauthorized(e):
    return render_template('website/_base.html', \
                            page=get_page_stub('errors/401')), 401


@current_app.errorhandler(403)
def page_forbidden(e):
    return render_template('website/_base.html', \
                            page=get_page_stub('errors/403')), 403


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
                            page=get_page_stub('errors/503')), 503
