from fabric.api import run, cd, env, lcd, sudo, put, local

'''
TO DEPLOY:
    fab dev/prod deploy

TO RESTART BACKEND
    fab dev/prod restart

TODO
 1. configure the ip's, remote app directory , ssh key etc
 2. add git tag support  - for easy rolleback
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
    ################################
    run('rm -rf /opt/tmp/cache/*')
    ################################


def deploy():

    run('cd %s; git checkout %s' % (remote_app_dir,env.branch))
    run('cd %(path)s; git pull' % {'path': remote_app_dir})
    restart()
    clearcache()
