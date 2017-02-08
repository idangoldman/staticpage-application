from fabric.api import *

from deployment import machine, ssl, nginx, uwsgi, git, virtualenv, mysql, frontend, user_folder_backup


@task
def setup():
    machine.setup()
    nginx.setup()
    # ssl.setup()
    git.setup()
    virtualenv.setup()
    uwsgi.setup()
    mysql.setup()
    frontend.setup()
    machine.info()


@task
def deploy():
    backup()
    frontend.deploy()
    git.deploy()
    virtualenv.install_packages()
    uwsgi.restart()
    mysql.migrate()


@task
def backup():
    mysql.backup()
    user_folder_backup()
