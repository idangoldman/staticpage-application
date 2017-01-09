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
    files.append('/etc/hosts', '127.0.0.1 staticpage.vagrant', use_sudo=True, escape=True)

def install_packages():
    packages = {
        'ubuntu': ' '.join([
            'build-essential',
            'git',
            'libffi-dev',
            'libmysqlclient-dev',
            'libssl-dev',
            'mariadb-server',
            'nginx',
            'python-dev',
            'python-minimal',
            'python-pip',
            'python',
            'software-properties-common',
            'uwsgi',
            'uwsgi-plugin-python'
        ]),
        'pip': ' '.join([
            'pip',
            'virtualenv'
        ])
    }

    sudo('apt-get install -y {0}'.format( packages['ubuntu'] ))
    run('pip install {0}'.format( packages['pip'] ))

def create_folders():
    if not files.exists('/home/ubuntu/logs'):
        run('mkdir /home/ubuntu/logs')

def setup_machine():
    machine_info()
    update_upgrade()
    set_hostname()
    create_folders()
    install_packages()


def update_nginx_template():
    kwargs = {
        'filename': './nginx.jnj',
        'destination': '/etc/nginx/sites-available/staticpage',
        'template_dir': './deployment/templates',
        'context': {
            'access_log_path': '/home/ubuntu/logs/nginx_access',
            'domain': 'staticpage.vagrant',
            'error_log_path': '/home/ubuntu/logs/nginx_error',
            'socket_path': '/tmp/backend.sock',
            'www_path': '/home/ubuntu/staticpage'
        },
        'use_jinja': True,
        'use_sudo': True,
        'backup': False
    }

    files.upload_template( **kwargs )
    # sudo('service nginx restart')


def setup_nginx():
    # sudo('service nginx status')
    if files.exists('rm -f /etc/nginx/sites-enabled/default'):
        sudo('rm -f /etc/nginx/sites-enabled/default')
    if not files.is_link('/etc/nginx/sites-enabled/staticpage'):
        update_nginx_template()
        sudo('ln -s /etc/nginx/sites-available/staticpage /etc/nginx/sites-enabled')
        sudo('service nginx restart')


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

def git_clone():
    if not files.exists('/home/ubuntu/staticpage'):
        prompts_dict = {
            'Are you sure you want to continue connecting (yes/no)? ': 'yes'
        }
        with cd('/home/ubuntu'), settings(prompts = prompts_dict):
            run('git clone %s' % 'git@github.com:idangoldman/staticpage.git')
            sudo('chown ubuntu:www-data staticpage')

def git_update():
    with cd('/home/ubuntu/staticpage'):
        run('git checkout deployment')
        run('git pull')

def setup_git():
    create_ssh_key()
    git_clone()
    git_update()


def setup_backend():
    with cd('/home/ubuntu/staticpage'):
        if not files.exists('venv'):
            run('virtualenv venv')
        if not files.exists('flask_env'):
            run('cp flask_env.example flask_env')

        with prefix('source venv/bin/activate'):
            run('pip install -r requirements.txt')
            run('deactivate')


def update_uwsgi_template():
    kwargs = {
        'filename': './uwsgi.jnj',
        'destination': '/etc/uwsgi/apps-available/staticpage.ini',
        'template_dir': './deployment/templates',
        'context': {
            'log_path': '/home/ubuntu/logs/uwsgi',
            'socket_path': '/tmp/backend.sock',
            'user': 'ubuntu',
            'group': 'www-data',
            'virtualenv_path': '/home/ubuntu/staticpage/venv',
            'www_path': '/home/ubuntu/staticpage'
        },
        'use_jinja': True,
        'use_sudo': True,
        'backup': False
    }

    files.upload_template( **kwargs )
    # sudo('service uwsgi restart')

def setup_uwsgi():
    # sudo('service uwsgi status')

    if not files.is_link('/etc/uwsgi/apps-enabled/staticpage.ini'):
        update_uwsgi_template()
        sudo('ln -s /etc/uwsgi/apps-available/staticpage.ini /etc/uwsgi/apps-enabled')
        sudo('service uwsgi restart')


def setup():
    setup_machine()
    setup_nginx()
    setup_git()
    setup_backend()
    setup_uwsgi()
