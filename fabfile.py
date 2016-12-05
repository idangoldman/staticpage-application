from fabric.api import run, cd, env, lcd, sudo, put, local

'''
TO DEPLOY:
    fab dev/prod deploy

TO RESTART BACKEND
    fab dev/prod restart
=======
from fabric.api import run, cd, env, sudo
import os


TO DEPLOY:
    fab prod deploy

TO RESTART BACKEND
    fab prod restart

TODO
 1. configure the ip's, remote app directory , ssh key etc
 2. add git tag support  - for easy rolleback
 3. run pip -r requirments.txt in env ??

'''

remote_app_dir ='/home/ubuntu/static-pages'
env.key_filename = '~/.ssh/static.pem' ## ssh key file (chmod 400)
env.user = 'ubuntu' #remote user



def prod():
    env.hosts = ['34.193.226.105']
    env.branch = 'fabric'

def dev():
    env.hosts = ['dev-server-ip'] # replace with IP address or hostname
    env.branch = 'dev'

def restart():
    run('sudo systemctl restart backend')

def clearcache():
    pass


def deploy():
    run('cd %s; git checkout %s' % (remote_app_dir, env.branch))
    run('cd %(path)s; git pull' % {'path': remote_app_dir})
    install_backend()
    restart()
    clearcache()

def git_clone():
    run('git clone %(git_repo)s %(remote_app_dir)s' % env)

def git_checkout_latest():
    run('cd %(remote_app_dir)s; git checkout %(branch)s; git pull origin %(branch)s' % env)


def install_backend():
    run('cd %s; venv/bin/pip install -r requirements.txt' % (remote_app_dir))
    run('pwd')

def install_frontend():
    pass
    run('cd %s' % remote_app_dir)
    run('npm install; bundle update')

def setup():
    git_clone()
    install_backend()
    install_frontend()
