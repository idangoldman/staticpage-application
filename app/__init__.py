from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_wtf import FlaskForm
from flask_wtf.csrf import CsrfProtect
from wtforms import StringField, validators

from config import config

def create_app( config_name ):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config[config_name])

    Bootstrap(app)
    CORS(app)
    CsrfProtect(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .root import root as root_blueprint
    app.register_blueprint(root_blueprint)

    return app