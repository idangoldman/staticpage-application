from fabric.api import *
from fabric.contrib import files


@task
def deploy():
    # local('gulp build --dist')
    if not files.exists('/home/ubuntu/staticpage/static'):
        run('mkdir /home/ubuntu/staticpage/static')
        sudo('chown ubuntu:www-data /home/ubuntu/staticpage/static')

    put('dist/*', '/home/ubuntu/staticpage/static')
