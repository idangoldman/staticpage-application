from fabric.api import *
from fabric.contrib import files

from deployment import machine, nginx, uwsgi, git, virtualenv, mysql, frontend


@task
def vagrant():
    env.use_ssh_config = True
    env.hosts = ['vagrant_ubuntu']


@task
def setup():
    machine.setup()
    nginx.setup()
    git.setup()
    virtualenv.setup()
    uwsgi.setup()
    mysql.setup()
    frontend.setup()
    machine.info()


@task
def deploy():
    frontend.deploy()
    git.deploy()
    uwsgi.restart()
    mysql.migrate()
