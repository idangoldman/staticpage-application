from fabric.api import *
from fabric.contrib import files


@task
def setup():
    create_static_folder()


@task
def create_static_folder():
    if not files.exists('/home/ubuntu/staticpage/static'):
        run('mkdir /home/ubuntu/staticpage/static')
        sudo('chown ubuntu:www-data /home/ubuntu/staticpage/static')


@task
def deploy():
    local('gulp build --dist')
    put('dist/*', '/home/ubuntu/staticpage/static')
