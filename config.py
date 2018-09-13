import os


class Config( object ):
    API_URL = os.environ['API_URL']
    BLOG_URL = os.environ['BLOG_URL']
    BASE_PATH = os.path.dirname( os.path.abspath( __file__ ) )
    HTTP_HOST = os.environ['HTTP_HOST']
    MAX_CONTENT_LENGTH = os.environ['FLASK_MAX_CONTENT_LENGTH']
    USER_FOLDER = os.environ['USER_FOLDER']

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 3rd Party
    # TODO: make them part of DB table - page
    GOOGLE_ANALYTICS_ID = os.environ['GOOGLE_ANALYTICS_ID']
    MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
    MAILCHIMP_LIST_ID = os.environ['MAILCHIMP_LIST_ID']
    MAILCHIMP_USERNAME = os.environ['MAILCHIMP_USERNAME']

    # MAIL
    MAIL_DEFAULT_SENDER = os.environ['MAIL_DEFAULT_SENDER']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_PORT = os.environ['MAIL_PORT']
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ['MAIL_USERNAME']


class DevelopmentConfig( Config ):
    DEBUG = True
    SECRET_KEY = os.environ['FLASK_SECRET_KEY'] or 'blah'
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ['FLASK_SECRET_KEY']
    SQLALCHEMY_ECHO = False
