import os
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # 3rd Party
    # TODO: make them part of DB table - page
    ADDTHIS_PUBID = os.getenv('ADDTHIS_PUBID')
    GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID')
    MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')
    MAILCHIMP_LIST_ID = os.getenv('MAILCHIMP_LIST_ID')
    MAILCHIMP_USERNAME = os.getenv('MAILCHIMP_USERNAME')


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY') or 'blah'


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}