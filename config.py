import os


class Config( object ):
    API_URL = os.getenv('API_URL')
    BLOG_URL = os.getenv('BLOG_URL')
    BASE_PATH = os.path.dirname( os.path.abspath( __file__ ) )
    HTTP_HOST = os.getenv('HTTP_HOST')
    MAX_CONTENT_LENGTH = os.getenv('FLASK_MAX_CONTENT_LENGTH')
    USER_FOLDER = os.getenv('USER_FOLDER')

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 3rd Party
    # TODO: make them part of DB table - page
    GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID')
    MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')
    MAILCHIMP_LIST_ID = os.getenv('MAILCHIMP_LIST_ID')
    MAILCHIMP_USERNAME = os.getenv('MAILCHIMP_USERNAME')

    # MAIL
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')


class DevelopmentConfig( Config ):
    DEBUG = True
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY') or 'blah'
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_ECHO = False
