from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app( config_name ):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_name)

    Bootstrap(app)
    CORS(app)
    CsrfProtect(app)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from app.helpers import jinja_filters
        from app import routes

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.root import root as root_blueprint
    app.register_blueprint(root_blueprint)

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
