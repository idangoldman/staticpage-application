from werkzeug.contrib.fixers import ProxyFix
import os

from backend import create_app, db
from backend.helpers import load_env_var


# loading environmental variables
load_env_var()

# creating backend app
app = create_app( os.getenv('FLASK_CONFIG') )
app.wsgi_app = ProxyFix( app.wsgi_app )


if __name__ == '__main__':
    from flask_migrate import Migrate, MigrateCommand
    from flask_script import Manager, Server

    manager = Manager( app )
    migrate = Migrate( app, db )

    manager.add_command( 'db', MigrateCommand )
    manager.add_command( 'runserver', Server( host = '0.0.0.0', port = 5000 ) )

    manager.run()
