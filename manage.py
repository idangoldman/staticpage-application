from werkzeug.contrib.fixers import ProxyFix
import os

from backend import create_app, db

# creating backend app
app = create_app( os.environ['FLASK_CONFIG'] )
app.wsgi_app = ProxyFix( app.wsgi_app )


if __name__ == '__main__':
    from flask_migrate import Migrate, MigrateCommand
    from flask_script import Manager, Server

    manager = Manager( app )
    migrate = Migrate( app, db )

    server_options = {
        'host': '0.0.0.0',
        'port': 5000,
        'threaded': True,
        'ssl_crt': './ssl/staticpage.local.crt',
        'ssl_key': './ssl/staticpage.local.key'
    }

    manager.add_command( 'db', MigrateCommand )
    manager.add_command( 'runserver', Server( **server_options ) )

    manager.run()
