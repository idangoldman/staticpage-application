from flask import Flask, Blueprint, render_template, redirect, make_response
from flask_assets import Environment, Bundle
from wtforms import Form, StringField, validators

from werkzeug.contrib.fixers import ProxyFix
import inspect, os

from app.controllers.static import static_pages
from app.controllers.general import *

import app.controllers.admin as dashboard
from app.models import *
from flask_wtf.csrf import CsrfProtect
from wtforms.csrf.session import SessionCSRF
from flask import session



def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(os.environ['APP_SETTINGS'])
    print(os.environ['APP_SETTINGS'])
    #from app.models import User
    assets = Environment(app)
    assets.versions = 'timestamp'
    assets.init_app(app)
    from flask_admin import Admin
    admin = Admin(app)
    db = MongoEngine()
    db.init_app(app)
    CsrfProtect(app)
    from app.models import db
    admin.add_view(dashboard.adminPage(name='Page'))
    admin.add_view(dashboard.UserView(User))
    return app

app = create_app()
app.register_blueprint(static_pages, url_prefix='/pages')
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config['root_path'] = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

class NewsletterForm(Form):
    email = StringField("email", [validators.Required(), validators.Email("Please enter your email address.")])
    class Meta:
        csrf = True  # Enable CSRF
        csrf_secret = app.config['CSRF_SECRET_KEY']
        csrf_class = SessionCSRF
        @property
        def csrf_context(self):
            return session

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form = NewsletterForm(request.form)
    if request.method == 'POST' and form.validate():
        if mailchimp_subscribe(form.email.data):
            return redirect('/thank-you')

    return render_template('pages/welcome.html', form=form, ga_id=app.config['GOOGLE_ANALYTICS_ID'], pub_id=app.config['ADDTHIS_PUBID'], has_subscribed=request.cookies.get('has_subscribed'))

@app.route('/thank-you')
def thank_you():
    response = make_response(render_template('pages/thank-you.html', pub_id=app.config['ADDTHIS_PUBID'], ga_id=app.config['GOOGLE_ANALYTICS_ID']))
    response.set_cookie('has_subscribed', 'true')
    return response

@app.route('/')
def index_route():
    return redirect('/welcome')

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('pages/errors/403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/errors/404.html'), 404

@app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('pages/errors/500.html'), 500

@app.errorhandler(503)
def page_service_unavailable(e):
    return render_template('pages/errors/503.html'), 503


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