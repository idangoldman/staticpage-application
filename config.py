import os
import inspect

class Config(object):
    API_URL = os.getenv('API_URL')
    root_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    UPLOAD_FOLDER = root_path + os.getenv('FLASK_UPLOAD_FOLDER')
    MAX_CONTENT_LENGTH = os.getenv('FLASK_MAX_CONTENT_LENGTH')

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

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY') or 'blah'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
