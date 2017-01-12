from fabric.api import *


def config():
    env.use_ssh_config = True


@task
def staging():
    config()
    env.hosts = ['vagrant_ubuntu']


@task
def production():
    config()
    env.hosts = ['linode']
