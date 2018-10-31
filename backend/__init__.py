from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
mail = Mail()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app( config_name ):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_name)

    CORS(app)
    CSRFProtect(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from backend.website import website as website_blueprint
        app.register_blueprint( website_blueprint )

        from backend.helpers import jinja
        from backend import routes

    from backend.auth import auth as auth_blueprint
    app.register_blueprint( auth_blueprint )

    from backend.api import api as api_blueprint
    app.register_blueprint( api_blueprint )

    return app
