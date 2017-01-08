import os
from fabric.api import *
from fabric.contrib.files import upload_template, exists

def vagrant():
    env.use_ssh_config = True
    env.hosts = ['vagrant_ubuntu']

def machine_info():
    run('uptime')
    run('uname -a')

def update_upgrade():
    sudo('apt-get update')
    sudo('apt-get -y upgrade')

def set_hostname():
    sudo('echo "staticpage.vagrant" > /etc/hostname')
    sudo('hostname -F /etc/hostname')
    run('hostname')
    sudo('echo "127.0.0.1 staticpage.vagrant" >> /etc/hosts')

def install_packages():
    packages = {
        'ubuntu': ' '.join([
            'software-properties-common',
            'git',
            'build-essential',
            'python',
            'python-minimal',
            'python-pip',
            'python-dev',
            'nginx',
            'mariadb-server'
        ]),
        'pip': ' '.join([
            'pip',
            'uwsgi',
            'virtualenv'
        ])
    }

    sudo('apt-get install -y {0}'.format( packages['ubuntu'] ))
    run('pip install {0}'.format( packages['pip'] ))

def setup_machine():
    machine_info()
    update_upgrade()
    set_hostname()
    install_packages()
    nginx_setup()

def nginx_setup():
    # sudo('service nginx status')
    update_nginx_template()
    if exists('rm -f /etc/nginx/sites-enabled/default'):
        sudo('rm -f /etc/nginx/sites-enabled/default')
    if not exists('/etc/nginx/sites-enabled/staticpage'):
        sudo('ln -s /etc/nginx/sites-available/staticpage /etc/nginx/sites-enabled')
    sudo('service nginx restart')

def update_nginx_template():
    template_variables = {
        'filename': './nginx.jnj',
        'destination': '/etc/nginx/sites-available/staticpage',
        'template_dir': './deployment/templates',
        'context': {
            'domain': 'staticpage.vagrant',
            'www_path': '/home/ubuntu/staticpage'
        },
        'use_jinja': True,
        'use_sudo': True,
        'backup': False
    }

    upload_template( **template_variables )
