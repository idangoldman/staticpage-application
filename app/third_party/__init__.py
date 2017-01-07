from flask import Flask, request
from flask import current_app as app
from flask_cors import CORS

from mailchimp3 import MailChimp
from validate_email import validate_email


def mailchimp_subscribe(email):
    if email and validate_email(email):
        client = MailChimp(app.config['MAILCHIMP_USERNAME'], app.config['MAILCHIMP_API_KEY'])
        try:
            client.lists.members.create(app.config['MAILCHIMP_LIST_ID'], {
                'email_address': email,
                'status': 'subscribed'
            })
        except Exception as e:
            # TODO: Check if user exist and return true otherwise false
            return True
        return True
    else:
        return False
