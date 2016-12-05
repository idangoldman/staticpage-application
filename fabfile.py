<<<<<<< HEAD
from fabric.api import run, cd, env, lcd, sudo, put, local

'''
TO DEPLOY:
    fab dev/prod deploy

TO RESTART BACKEND
    fab dev/prod restart
=======
from fabric.api import run, cd, env, sudo
import os

'''
TO DEPLOY:
    fab prod deploy

TO RESTART BACKEND
    fab prod restart
>>>>>>> 2d4399eda73d90f47c185f7beb64f99b8aebf7ff

TODO
 1. configure the ip's, remote app directory , ssh key etc
 2. add git tag support  - for easy rolleback
<<<<<<< HEAD
 3. run pip -r requirments.txt in env ??

'''

remote_app_dir ='/opt/app'
env.key_filename = '~/.ssh/production.pem' ## ssh key file (chmod 400)
env.user = 'ubuntu' #remote user



def prod():
    env.hosts = ['prod-server-ip']
    env.branch = 'master'

def dev():
    env.hosts = ['dev-server-ip'] # replace with IP address or hostname
    env.branch = 'dev'

def restart():
    run('sudo restart backend')

def clearcache():
=======

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
>>>>>>> 2d4399eda73d90f47c185f7beb64f99b8aebf7ff
    ################################
    run('rm -rf /opt/tmp/cache/*')
    ################################

<<<<<<< HEAD

def deploy():

    run('cd %s; git checkout %s' % (remote_app_dir,env.branch))
    run('cd %(path)s; git pull' % {'path': remote_app_dir})
    restart()
    clearcache()
=======
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
>>>>>>> 2d4399eda73d90f47c185f7beb64f99b8aebf7ff
