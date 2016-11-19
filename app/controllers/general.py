from flask import Flask, request
from flask import current_app as app
from flask_cors import CORS

from mailchimp import Mailchimp
from validate_email import validate_email

from pprint import pprint


def mailchimp_subscribe(email):
    if email and validate_email(email):
        api_key = app.config['MAILCHIMP_API_KEY']
        payload = {
            "id": app.config['MAILCHIMP_LIST_ID'],
            "email": {
                "email": email
            },
        }
        mc = Mailchimp(api_key, True)
        mc.call('lists/subscribe', payload)
        return True
    else:
        return False