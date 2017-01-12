from fabric.api import *

from deployment import machine, nginx, uwsgi, git, virtualenv, mysql, frontend


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
