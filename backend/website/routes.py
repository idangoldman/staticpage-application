from flask import render_template, current_app, redirect, make_response, json, request, url_for
from flask_login import current_user

from backend.third_party import mailchimp_subscribe
from backend.website import website
from backend.website.forms import NewsletterForm


def get_page_stub( name ):
    with open('backend/stubs/features.json', 'r') as json_file:
        features = json.load( json_file )
    with open('backend/stubs/website/' + name + '.json', 'r') as json_file:
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


@website.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form = NewsletterForm(request.form)

    if request.method == 'POST' and form.validate():
        if mailchimp_subscribe(form.email.data):
            return redirect( url_for('website.create_a_page') )

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'pub_id': current_app.config['ADDTHIS_PUBID'],
        'has_subscribed': request.cookies.get('has_subscribed'),
        'page': get_page_stub('welcome'),
    }

    return render_template('website/welcome.html', **payload)


@website.route('/create-a-page')
def create_a_page():
    return render_template('website/create-a-page.html')


@website.route('/register')
def register():
    payload = {
        'page': get_page_stub('register'),
    }

    return render_template('website/_base.html', **payload)
