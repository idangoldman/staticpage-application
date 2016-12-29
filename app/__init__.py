from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

db = SQLAlchemy()

def create_app( config_name ):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_name)

    Bootstrap(app)
    CORS(app)
    CsrfProtect(app)
    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .root import root as root_blueprint
    app.register_blueprint(root_blueprint)

    return app