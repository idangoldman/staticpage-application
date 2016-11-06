import os


class Config(object):
    MONGODB_SETTINGS = {'DB': 'testing'}
    SECRET_KEY = "w2525ferg3456t354y"

class DevConfig(Config):
    DEBUG = True
    MAILCHIMP_MAILING_LIST_ID = 12
    MAILCHIMP_API_KEY = '2134fsdcsdcsvcsdf'