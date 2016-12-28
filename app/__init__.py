from flask import Flask
from flask_cors import CORS
from flask_wtf import FlaskForm
from flask_wtf.csrf import CsrfProtect
from wtforms import StringField, validators

from config import config

def create_app( config_name ):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config[config_name])

    CORS(app)
    CsrfProtect(app)

    return app