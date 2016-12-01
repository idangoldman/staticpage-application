import os


class Config(object):
    MONGODB_SETTINGS = {'DB': 'testing'}
    SECRET_KEY = "w2525ferg3456t354y"
    MAILCHIMP_LIST_ID = os.environ['MAILCHIMP_LIST_ID']
    MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
    MAILCHIMP_USERNAME = os.environ['MAILCHIMP_USERNAME']
    GOOGLE_ANALYTICS_ID = os.environ['GOOGLE_ANALYTICS_ID']
    ADDTHIS_PUBID = os.environ['ADDTHIS_PUBID']

class DevConfig(Config):
    DEBUG = True