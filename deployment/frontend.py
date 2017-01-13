from fabric.api import *
from fabric.contrib import files


@task
def setup():
    create_static_folder()


@task
def create_static_folder():
    if not files.exists( env.static_folder ):
        run( 'mkdir %(static_folder)s' % env )
        sudo( 'chown %(user)s:%(user_group)s %(static_folder)s' % env )


@task
def deploy():
    local('gulp build --dist')
    put( 'dist/*', env.static_folder )
