print(' - Start')

import click
import inspect, os

from flask import Flask, Blueprint, render_template, redirect, make_response, json, request, jsonify

from werkzeug.contrib.fixers import ProxyFix

from flask_wtf import FlaskForm
from flask_wtf.csrf import CsrfProtect
from wtforms import StringField, validators


from app.third_party import mailchimp_subscribe, load_env_var
from app import create_app
load_env_var()

app = create_app(os.getenv('FLASK_CONFIG'))
app.config['root_path'] = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
app.wsgi_app = ProxyFix(app.wsgi_app)

# Jinja custom filters
import re
from jinja2 import evalcontextfilter, Markup
import markdown as markdown_lib

@app.template_filter()
@evalcontextfilter
def markdown(eval_ctx, value):
    return Markup(markdown_lib.markdown(value))

@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    value = re.sub(r'\r\n|\r|\n', '\n', value)
    param = re.split('\n{2,}', value)
    param = [u'%s' % p.replace('\n', '<br />') for p in param]
    param = u'\n\n'.join(param)
    return Markup(param)


class NewsletterForm(FlaskForm):
    email = StringField("email", [validators.Required(), validators.Email("Please enter your email address.")])

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form = NewsletterForm(request.form)

    if request.method == 'POST' and form.validate():
        if mailchimp_subscribe(form.email.data):
            return redirect('/thank-you')

    with open('app/features.json', 'r') as json_file:
        features = json.load( json_file )
    with open('app/user_page.json', 'r') as json_file:
        user_page = json.load( json_file )

    for feature in features:
        if feature['name'] in user_page:
            for field in feature['fields']:
                if field['name'] in user_page[feature['name']]:
                    if not user_page[feature['name']][field['name']] and 'default' in field:
                        user_page[feature['name']][field['name']] = field['default']

    payload = {
        'form': form,
        'ga_id': app.config['GOOGLE_ANALYTICS_ID'],
        'pub_id': app.config['ADDTHIS_PUBID'],
        'has_subscribed': request.cookies.get('has_subscribed'),
        'content': user_page['content'],
        'design': user_page['design']
    }

    return render_template('pages/welcome.html', **payload)


@app.route('/thank-you')
def thank_you():
    payload = {
        'pub_id': app.config['ADDTHIS_PUBID'],
        'ga_id': app.config['GOOGLE_ANALYTICS_ID']
    }

    response = make_response(render_template('pages/thank-you.html', **payload))
    response.set_cookie('has_subscribed', 'true')
    return response


@app.route('/')
@app.route('/pages')
def index_route():
    return redirect('/welcome')


@app.route('/home')
def home():
    return render_template('pages/home.html')


@app.route('/side-kick')
def side_kick():
    with open('static/images/side-kick-sprite.svg', 'r') as svg_file:
        svg_sprite = svg_file.read()
    with open('app/features.json', 'r') as json_file:
        features = json.load( json_file )
    with open('app/user_page.json', 'r') as json_file:
        user_page = json.load( json_file )

    for feature in features:
        if feature['name'] in user_page:
            for field in feature['fields']:
                if field['name'] in user_page[feature['name']]:
                    field['value'] = user_page[feature['name']][field['name']]
            # if feature['name'] is 'search_results':
                # from pprint import pprint
                # pprint

    payload = {
        'svg_sprite': svg_sprite,
        'features': features
    }

    return render_template('pages/side-kick.html', **payload)


@app.route('/fake-api', methods=['POST'])
def fake_api():
    return jsonify( request.values )


@app.errorhandler(401)
def page_unauthorized(e):
    return render_template('pages/errors/401.html'), 401

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('pages/errors/403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/errors/404.html'), 404


@app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('pages/errors/500.html'), 500


@app.errorhandler(503)
def page_service_unavailable(e):
    return render_template('pages/errors/503.html'), 503


if __name__ == '__main__':
    app_options = {
        'host': '0.0.0.0',
        'port': 5000,
        'debug' : app.config['DEBUG']
    }

    app.run(**app_options)