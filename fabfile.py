from fabric.api import run, cd, env, sudo
import os

'''
TO DEPLOY:
    fab prod deploy

TO RESTART BACKEND
    fab prod restart

TODO
 1. configure the ip's, remote app directory , ssh key etc
 2. add git tag support  - for easy rolleback

'''

env.remote_app_dir = '/opt/app'
env.git_repo = os.environ['GIT_REPO_PATH']
env.key_filename = os.environ['SSH_KEY_PATH'] ## ssh key file (chmod 400)
env.user = 'deploy' #remote user


def prod():
    env.hosts = os.environ['SERVER_IP']
    env.branch = 'master'

def restart():
    run('sudo restart backend')

def clear_cache():
    ################################
    run('rm -rf /opt/tmp/cache/*')
    ################################

def git_clone():
    run('git clone %(git_repo)s %(remote_app_dir)s' % env)

def git_checkout_latest():
    run('cd %(remote_app_dir)s; git checkout %(branch)s; git pull origin %(branch)s' % env)

def deploy():
    git_checkout_latest()
    restart()
    clear_cache()

def install_backend():
    run('cd %' % env.remote_app_dir)
    run('pip install -r requirements.txt')

def install_frontend():
    run('cd %' % env.remote_app_dir)
    run('npm install; bundle update')

def setup():
    git_clone()
    install_backend()
    install_frontend()