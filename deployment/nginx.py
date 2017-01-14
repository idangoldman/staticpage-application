from fabric.api import *
from fabric.contrib import files


@task
def setup():
    if files.exists('rm -f /etc/nginx/sites-enabled/default'):
        sudo('rm -f /etc/nginx/sites-enabled/default')
    if not files.is_link('/etc/nginx/sites-enabled/%(product_name)s' % env):
        update_gzip_file()
        update_site_file()
        sudo('ln -s /etc/nginx/sites-available/%(product_name)s /etc/nginx/sites-enabled' % env)
        restart()


@task
def update_gzip_file():
    kwargs = {
        'filename': 'gzip.jnj',
        'destination': '/etc/nginx/snippets/gzip.conf',
        'template_dir': 'deployment/templates',
        'use_sudo': True,
        'backup': False
    }

    files.upload_template( **kwargs )

@task
def update_site_file():
    kwargs = {
        'filename': 'nginx.jnj',
        'destination': '/etc/nginx/sites-available/' + env.product_name,
        'template_dir': 'deployment/templates',
        'context': {
            'access_log_path': env.logs_folder + '/nginx_access',
            'domain': env.domain,
            'error_log_path': env.logs_folder + '/nginx_error',
            'socket_path': '/tmp/backend.sock',
            'www_path': env.remote_folder
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
@task
def test():
    sudo('nginx -t')
