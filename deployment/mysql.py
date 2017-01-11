from fabric.api import *
from fabric.contrib import files


@task
def setup():
    install()
    secure_installation()
    create_db()
    restart()


@task
def install():
    sudo('apt-get install -y mysql-server')


@task
def secure_installation():
    prompts_dict = {
        'Press y|Y for Yes, any other key for No: ': 'n',
        'Change the password for root ? ((Press y|Y for Yes, any other key for No) : ': 'n',
        'Remove anonymous users? (Press y|Y for Yes, any other key for No) : ': 'y',
        'Disallow root login remotely? (Press y|Y for Yes, any other key for No) : ': 'n',
        'Remove test database and access to it? (Press y|Y for Yes, any other key for No) : ': 'y',
        'Reload privilege tables now? (Press y|Y for Yes, any other key for No) : ': 'y'
    }

    with settings( prompts = prompts_dict ):
        sudo('mysql_secure_installation')


@task
def create_db():
    run('mysql -u root -p -e "CREATE DATABASE staticpage;"')


@task
def migrate():
    with cd('/home/ubuntu/staticpage'), prefix('source venv/bin/activate'):
        run('python manage.py db upgrade')


@task
def start():
    sudo('service mysql start')
@task
def restart():
    sudo('service mysql restart')
@task
def stop():
    sudo('service mysql stop')
@task
def status():
    sudo('service mysql status')
