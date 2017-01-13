from datetime import datetime
from fabric.api import *


def config():
    env.timestamp = datetime.now().strftime('%Y.%m.%d %H:%M')
    env.product_name = 'staticpage'

    env.use_ssh_config = True
    env.user = 'ubuntu'
    env.user_group = 'www-data'

    env.db_name = 'staticpage'
    env.db_user = 'root'

    env.branch = 'master'
    env.git_repo = 'git@github.com:idangoldman/staticpage.git'

    env.local_folder = '~/Documents/' + env.product_name
    env.remote_folder = '/home/ubuntu/staticpage'
    env.home_folder = '/home/' + env.user
    env.logs_folder = '/home/ubuntu/logs'
    env.static_folder = env.remote_folder + '/static'


@task
def staging():
    config()
    env.name = 'staging'
    env.hosts = ['vagrant_ubuntu']
    env.ssh_key_email = 'ubuntu@ubuntu.vagrant'
    env.domain = 'staticpage.vagrant'
    env.domain_ip = '127.0.0.1'


@task
def production():
    config()
    env.name = 'production'
    env.hosts = ['linode']
    env.ssh_key_email = 'ubuntu@ubuntu.linode'
    env.domain = 'staticpage.info'
    env.domain_ip = '139.162.173.136'