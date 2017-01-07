import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from backend import create_app, db
from backend.helpers import load_env_var
load_env_var()


app = create_app( os.getenv('FLASK_CONFIG') )

manager = Manager( app )
migrate = Migrate( app, db )


manager.add_command( 'db', MigrateCommand )

if __name__ == '__main__':
    manager.run()
