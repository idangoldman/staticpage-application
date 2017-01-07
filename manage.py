import os
from werkzeug.contrib.fixers import ProxyFix

from backend import create_app
from backend.helpers import load_env_var


# loading environmental variables
load_env_var()

# starting the backend
app = create_app( os.getenv('FLASK_CONFIG') )
app.wsgi_app = ProxyFix( app.wsgi_app )


if __name__ == '__main__':
    app_options = {
        'host': '0.0.0.0',
        'port': 5000,
        'debug' : app.config['DEBUG']
    }

    app.run( **app_options )
