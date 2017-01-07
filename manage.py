import os
from werkzeug.contrib.fixers import ProxyFix

from app.helpers import load_env_var
from app import create_app


# loading environmental variables
load_env_var()

# starting the backend
app = create_app(os.getenv('FLASK_CONFIG'))
app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    app_options = {
        'host': '0.0.0.0',
        'port': 5000,
        'debug' : app.config['DEBUG']
    }

    app.run(**app_options)
