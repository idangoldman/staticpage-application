from fabric.api import *
from fabric.contrib import files


@task
def setup():
    install()
    status()
    # secure_installation()
    # create_db();
    # restart()
    # start()


def install():
    sudo('apt-get install -y mysql-server')


def secure_installation():
    prompts_dict = {
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
