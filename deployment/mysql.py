from fabric.api import *
from fabric.contrib import files


@task
def setup():
    install()
    secure_installation()
    create_db()
    restart()


def install():
    sudo('apt-get install -y mysql-server')


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


def create_db():
    run('mysql -u root -p -e "CREATE DATABASE staticpage;"')


def start():
    sudo('service mysql start')
def restart():
    sudo('service mysql restart')
def stop():
    sudo('service mysql stop')
def status():
    sudo('service mysql status')
