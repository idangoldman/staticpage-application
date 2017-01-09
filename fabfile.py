import os
from fabric.api import *
from fabric.contrib import files

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

def nginx_setup():
    # sudo('service nginx status')
    if files.exists('rm -f /etc/nginx/sites-enabled/default'):
        sudo('rm -f /etc/nginx/sites-enabled/default')
    if not files.exists('/etc/nginx/sites-enabled/staticpage'):
        update_nginx_template()
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

    files.upload_template( **template_variables )

def setup_machine():
    machine_info()
    update_upgrade()
    set_hostname()
    install_packages()
    nginx_setup()

def git_clone():
    if not files.exists('/home/ubuntu/staticpage'):
        prompts_dict = {
            'Are you sure you want to continue connecting (yes/no)? ': 'yes'
        }
        with cd('/home/ubuntu'), settings(prompts = prompts_dict):
            run('git clone %s' % 'git@github.com:idangoldman/staticpage.git')

def create_ssh_key(overwrite = False):
    if not files.exists('/home/ubuntu/.ssh/id_rsa.pub') or overwrite:
        prompts_dict = {
            'Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): ': '',
            'Enter passphrase (empty for no passphrase): ': '',
            'Enter same passphrase again: ': '',
            'Overwrite (y/n)? ': 'y'
        }

        with settings(prompts = prompts_dict):
            run('ssh-keygen -t rsa -b 4096 -C "ubuntu@ubuntu.vagrant"')

        id_rsa_pub = run('cat /home/ubuntu/.ssh/id_rsa.pub')
        print '###'
        print id_rsa_pub
        print '###'
        print ''
        with settings(abort_on_prompts=False):
            prompt('\n\nPaste in "Settings > Deploy keys" and hit enter')

def deploy():
    create_ssh_key()
    git_clone()
