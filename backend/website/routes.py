from flask import render_template, current_app, redirect, request, url_for
from flask_login import current_user

from backend.helpers import get_page_stub
from backend.third_party import mailchimp_subscribe
from backend.website import website
from backend.website.forms import NewsletterForm


@website.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form = NewsletterForm()

    if form.validate_on_submit():
        if mailchimp_subscribe(
            form.email.data,
            current_app.config['MAILCHIMP_USERNAME'],
            current_app.config['MAILCHIMP_API_KEY'],
            current_app.config['MAILCHIMP_LIST_ID']
        ):
            return redirect( url_for('auth.register', email=form.email.data) )

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'page': get_page_stub('website/welcome'),
        'show_login_link': request.cookies.get('show_login_link')
    }

    return render_template('website/welcome.html', **payload)
