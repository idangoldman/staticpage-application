from fabric.api import *
from fabric.contrib import files


@task
def setup():
    create()
    install_packages()

@task
def create():
    with cd( env.remote_folder ):
        if not files.exists('venv'):
            run('virtualenv venv')
        if not files.exists('flask_env'):
            run('cp flask_env.example flask_env')

@task
def install_packages():
    with cd( env.remote_folder ), prefix('source venv/bin/activate'):
        run('pip install -r requirements.txt')
        run('deactivate')
