import os

class Config(object):
    API_URL = os.getenv('API_URL')

    # SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    # 3rd Party
    # TODO: make them part of DB table - page
    ADDTHIS_PUBID = os.getenv('ADDTHIS_PUBID')
    GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID')
    MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')
    MAILCHIMP_LIST_ID = os.getenv('MAILCHIMP_LIST_ID')
    MAILCHIMP_USERNAME = os.getenv('MAILCHIMP_USERNAME')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False

    SECRET_KEY = os.getenv('SECRET_KEY') or 'blah'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False

    SECRET_KEY = os.getenv('SECRET_KEY')