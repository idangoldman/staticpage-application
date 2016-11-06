from flask import Flask, request
from flask_cors import CORS
from mailchimp import Mailchimp
from validate_email import validate_email
from flask import current_app as app

def mailchimp_subscribe(email):
    if email and validate_email(email):
        api_key = ''  # API Key
        payload = {
            "id": app.config['MAILCHIMP_MAILING_LIST_ID'],
            "email": {
                "email": email
            },
        }
        mc = Mailchimp(app.config['MAILCHIMP_API_KEY'], True)
        mc.call('lists/subscribe', payload)
        return True
    else:
        return False