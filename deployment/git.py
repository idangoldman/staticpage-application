from fabric.api import *
from fabric.contrib import files


@task
def setup():
    create_ssh_key()
    clone()
    update()


@task
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


@task
def clone():
    if not files.exists('/home/ubuntu/staticpage'):
        prompts_dict = {
            'Are you sure you want to continue connecting (yes/no)? ': 'yes'
        }
        with cd('/home/ubuntu'), settings(prompts = prompts_dict):
            run('git clone %s' % 'git@github.com:idangoldman/staticpage.git')
            sudo('chown ubuntu:www-data staticpage')


@task
def update():
    with cd('/home/ubuntu/staticpage'):
        run('git checkout master')
        run('git pull')


@task
def deploy():
    update()
