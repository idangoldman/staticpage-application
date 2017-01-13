from fabric.api import *


def config():
    env.product_name = 'staticpage'

    env.use_ssh_config = True
    env.user = 'ubuntu'
    env.user_group = 'www-data'

    env.branch = 'master'
    env.git_repo = 'git@github.com:idangoldman/staticpage.git'

    env.local_folder = ''
    env.remote_folder = '/home/ubuntu/staticpage'
    env.remote_home_folder = '/home/' + env.user
    env.logs_folder = '/home/ubuntu/logs'
    env.static_folder = env.remote_folder + '/static'


@task
def staging():
    config()
    env.hosts = ['vagrant_ubuntu']
    env.ssh_key_email = 'ubuntu@ubuntu.vagrant'
    env.domain = 'staticpage.vagrant'
    env.domain_ip = '127.0.0.1'


@task
def production():
    config()
    env.hosts = ['linode']
    env.ssh_key_email = 'ubuntu@ubuntu.linode'
    env.domain = 'staticpage.info'
    env.domain_ip = '139.162.173.136'
