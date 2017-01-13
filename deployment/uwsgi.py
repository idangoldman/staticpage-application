from fabric.api import *
from fabric.contrib import files


@task
def setup():
    # create_logs_folder()
    if not files.is_link('/etc/uwsgi/apps-enabled/%(product_name)s.ini' % env):
        update_conf_file()
        sudo('ln -s /etc/uwsgi/apps-available/%(product_name)s.ini /etc/uwsgi/apps-enabled' % env)
        sudo('service uwsgi restart')


@task
def update_conf_file():
    kwargs = {
        'filename': 'uwsgi.jnj',
        'destination': '/etc/uwsgi/apps-available/%(product_name)s.ini' % env,
        'template_dir': 'deployment/templates',
        'context': {
            # 'log_path': '/home/ubuntu/logs/uwsgi.log',
            'socket_path': '/tmp/backend.sock',
            'user': env.user,
            'group': env.user_group,
            'virtualenv_path': env.remote_folder + '/venv',
            'www_path': env.remote_folder
        },
        'use_jinja': True,
        'use_sudo': True,
        'backup': False
    }

    files.upload_template( **kwargs )


# @task
# def create_logs_folder():
#     if not files.exists('/home/ubuntu/logs/uwsgi.log'):
#         run('touch /home/ubuntu/logs/uwsgi.log')
#         sudo('chown ubuntu:www-data -R /home/ubuntu/logs/uwsgi.log')


@task
def start():
    sudo('service uwsgi start')
@task
def restart():
    sudo('service uwsgi restart')
@task
def stop():
    sudo('service uwsgi stop')
@task
def status():
    sudo('service uwsgi status')
