from fabric.api import *
from fabric.contrib import files


@task
def setup():
    update_and_upgrade()
    set_hostname()
    create_logs_folder()
    install_packages()


@task
def info():
    run('lsb_release -a')
    run('uname -a')
    run('uptime')


@task
def update_and_upgrade():
    sudo('apt-get update')
    sudo('apt-get -y upgrade')


@task
def set_hostname():
    sudo( 'echo "%(domain)s" > /etc/hostname' % env )
    sudo('hostname -F /etc/hostname')
    host = env.domain_ip + ' ' + env.domain
    files.append( '/etc/hosts', host, use_sudo=True, escape=True )


@task
def install_packages():
    packages = {
        'ubuntu': ' '.join([
            'build-essential',
            'git',
            'libffi-dev',
            'libmysqlclient-dev',
            'libssl-dev',
            'nginx-full',
            'python-dev',
            'python-minimal',
            'python-pip',
            'python',
            'software-properties-common',
            'uwsgi',
            'uwsgi-plugin-python',
            'vim'
        ]),
        'pip': ' '.join([
            'pip',
            'virtualenv'
        ])
    }

    sudo('apt-get install -y {0}'.format( packages['ubuntu'] ))
    run('pip install {0}'.format( packages['pip'] ))


@task
def create_logs_folder():
    if not files.exists( env.logs_folder ):
        run( 'mkdir %(logs_folder)s' % env )
