from fabric.api import *
from fabric.contrib import files


@task
def setup():
    # sudo('service nginx status')
    if files.exists('rm -f /etc/nginx/sites-enabled/default'):
        sudo('rm -f /etc/nginx/sites-enabled/default')
    if not files.is_link('/etc/nginx/sites-enabled/staticpage'):
        update_conf_file()
        sudo('ln -s /etc/nginx/sites-available/staticpage /etc/nginx/sites-enabled')
        sudo('service nginx restart')


@task
def update_conf_file():
    kwargs = {
        'filename': './nginx.jnj',
        'destination': '/etc/nginx/sites-available/staticpage',
        'template_dir': './templates',
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
    # sudo('service nginx restart')
