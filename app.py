from flask import Flask,Blueprint
from werkzeug.contrib.fixers import ProxyFix
from flask import render_template
import inspect, os

from app.controllers.static import static_pages
import app.controllers.admin as dashboard




def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    print(os.environ['APP_SETTINGS'])

    #from app.models import User
    from flask.ext.admin import Admin
    admin = Admin(app)
    admin.add_view(dashboard.adminPage(name='Page'))
    return app

app = create_app()
#mongo = PyMongo(app)
app.register_blueprint(static_pages,url_prefix='/pages')
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config['root_path'] =  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


@app.route("/")
def rootIndexNameNotImportant():
    obj = {
        "name" : "barak",
        "lname" : "bloch"
    }
    return render_template('index.html', obj=obj)

if __name__ == '__main__':
    # some stuff for debugger in pycharm
    import argparse
    parser = argparse.ArgumentParser(description='Development Server Help')
    parser.add_argument("-d", "--debug", action="store_true", dest="debug_mode",
                        help="run in debug mode (for use with PyCharm)", default=False)
    parser.add_argument("-p", "--port", dest="port",
                        help="port of server (default:%(default)s)", type=int, default=5000)

    cmd_args = parser.parse_args()
    app_options = {"host" : '0.0.0.0' , "port": cmd_args.port,"debug" : app.config['DEBUG']}

    if cmd_args.debug_mode:
        app_options["debug"] = True
        app_options["use_debugger"] = False
        app_options["use_reloader"] = False

    app.run(**app_options)