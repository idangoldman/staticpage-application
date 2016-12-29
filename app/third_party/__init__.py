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

# TODO: Move it to a better place
def load_env_var( env_file = '.env_flask' ):
    import os
    if os.path.exists(env_file):
        print(' * Importing environment from %s...' % env_file)
        for line in open(env_file):
            variables = line.strip().split('=')
            if len(variables) == 2:
                # print(variables[0])
                os.environ[variables[0]] = variables[1]