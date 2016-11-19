from flask import Flask, Blueprint, render_template, jsonify
from flask_assets import Environment, Bundle
from wtforms import Form, StringField, validators
from pprint import pprint

from werkzeug.contrib.fixers import ProxyFix
import inspect, os

from app.controllers.static import static_pages
from app.controllers.general import *

import app.controllers.admin as dashboard
from app.models import *

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(os.environ['APP_SETTINGS'])
    print(os.environ['APP_SETTINGS'])
    #from app.models import User
    assets = Environment(app)
    assets.init_app(app)
    from flask_admin import Admin
    admin = Admin(app)
    db = MongoEngine()
    db.init_app(app)
    from app.models import db
    admin.add_view(dashboard.adminPage(name='Page'))
    admin.add_view(dashboard.UserView(User))
    return app

app = create_app()
app.register_blueprint(static_pages,url_prefix='/pages')
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config['root_path'] = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

class NewsletterForm(Form):
    email = StringField("Email", [validators.Required(), validators.Email("Please enter your email address.")])

@app.route('/newsletter', methods=['POST'])
def subscribe_to_newsletter():
    email = request.form.get('email')
    pprint(email);
    return email
    # return jsonify( mailchimp_subscribe(email))

@app.route('/')
def index_route():
    form = NewsletterForm()
    return render_template('pages/home.html', form=form)

if __name__ == '__main__':
    # some stuff for debugger in pycharm
    import argparse
    parser = argparse.ArgumentParser(description='Development Server Help')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug_mode',
                        help='run in debug mode (for use with PyCharm)', default=False)
    parser.add_argument('-p', '--port', dest='port',
                        help='port of server (default:%(default)s)', type=int, default=5000)

    cmd_args = parser.parse_args()
    app_options = {'host' : '0.0.0.0' , 'port': cmd_args.port,'debug' : app.config['DEBUG']}

    if cmd_args.debug_mode:
        app_options['debug'] = True
        app_options['use_debugger'] = False
        app_options['use_reloader'] = False

    app.run(**app_options)