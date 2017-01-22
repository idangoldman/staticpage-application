import os


class Config( object ):
    API_URL = os.getenv('API_URL')
    BASE_PATH = os.path.dirname( os.path.abspath( __file__ ) )
    HTTP_HOST = os.getenv('HTTP_HOST')
    MAX_CONTENT_LENGTH = os.getenv('FLASK_MAX_CONTENT_LENGTH')
    UPLOAD_FOLDER = os.getenv('FLASK_UPLOAD_FOLDER')

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 3rd Party
    # TODO: make them part of DB table - page
    ADDTHIS_PUBID = os.getenv('ADDTHIS_PUBID')
    GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID')
    MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')
    MAILCHIMP_LIST_ID = os.getenv('MAILCHIMP_LIST_ID')
    MAILCHIMP_USERNAME = os.getenv('MAILCHIMP_USERNAME')


class DevelopmentConfig( Config ):
    DEBUG = True
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY') or 'blah'
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_ECHO = False
