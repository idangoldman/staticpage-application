from fabric.api import *
from fabric.contrib import files


@task
def setup():
    with cd('/home/ubuntu/staticpage'):
        if not files.exists('venv'):
            run('virtualenv venv')
        if not files.exists('flask_env'):
            run('cp flask_env.example flask_env')

        with prefix('source venv/bin/activate'):
            run('pip install -r requirements.txt')
            run('deactivate')
