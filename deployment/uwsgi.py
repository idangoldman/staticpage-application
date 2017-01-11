from fabric.api import *
from fabric.contrib import files


@task
def setup():
    # sudo('service uwsgi status')

    if not files.is_link('/etc/uwsgi/apps-enabled/staticpage.ini'):
        update_conf_file()
        sudo('ln -s /etc/uwsgi/apps-available/staticpage.ini /etc/uwsgi/apps-enabled')
        sudo('service uwsgi restart')


@task
def update_conf_file():
    kwargs = {
        'filename': 'uwsgi.jnj',
        'destination': '/etc/uwsgi/apps-available/staticpage.ini',
        'template_dir': 'deployment/templates',
        'context': {
            'log_path': '/home/ubuntu/logs/uwsgi',
            'socket_path': '/tmp/backend.sock',
            'user': 'ubuntu',
            'group': 'www-data',
            'virtualenv_path': '/home/ubuntu/staticpage/venv',
            'www_path': '/home/ubuntu/staticpage'
        },
        'use_jinja': True,
        'use_sudo': True,
        'backup': False
    }

    files.upload_template( **kwargs )
    # sudo('service uwsgi restart')
