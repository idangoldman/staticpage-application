from fabric.api import *
from fabric.contrib import files


@task
def setup():
    if files.exists('rm -f /etc/nginx/sites-enabled/default'):
        sudo('rm -f /etc/nginx/sites-enabled/default')
    if not files.is_link('/etc/nginx/sites-enabled/staticpage'):
        update_conf_file()
        sudo('ln -s /etc/nginx/sites-available/staticpage /etc/nginx/sites-enabled')
        restart()


@task
def update_conf_file():
    kwargs = {
        'filename': 'nginx.jnj',
        'destination': '/etc/nginx/sites-available/staticpage',
        'template_dir': 'deployment/templates',
        'context': {
            'access_log_path': '/home/ubuntu/logs/nginx_access',
            'domain': 'staticpage.vagrant',
            'error_log_path': '/home/ubuntu/logs/nginx_error',
            'socket_path': '/tmp/backend.sock',
            'www_path': '/home/ubuntu/staticpage'
        },
        'use_jinja': True,
        'use_sudo': True,
        'backup': False
    }

    files.upload_template( **kwargs )


@task
def start():
    sudo('service nginx start')
@task
def restart():
    sudo('service nginx restart')
@task
def stop():
    sudo('service nginx stop')
@task
def status():
    sudo('service nginx status')
