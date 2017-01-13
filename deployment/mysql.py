from fabric.api import *
from fabric.contrib import files


@task
def setup():
    install()
    secure_installation()
    create()
    restart()


@task
def install():
    sudo('apt-get install -y mysql-server')


@task
def secure_installation():
    prompts_dict = {
        'Press y|Y for Yes, any other key for No: ': 'n',
        'Change the password for root ? ((Press y|Y for Yes, any other key for No) : ': 'n',
        'Remove anonymous users? (Press y|Y for Yes, any other key for No) : ': 'y',
        'Disallow root login remotely? (Press y|Y for Yes, any other key for No) : ': 'y',
        'Remove test database and access to it? (Press y|Y for Yes, any other key for No) : ': 'y',
        'Reload privilege tables now? (Press y|Y for Yes, any other key for No) : ': 'y'
    }

    with settings( prompts = prompts_dict ):
        sudo('mysql_secure_installation')


@task
def create():
    run( 'mysql -u %(db_user)s -p -e "CREATE DATABASE %(db_name)s;"' % env )

@task
def backup():
    with cd( env.home_folder ):
        remote_file = '/'.join([ env.home_folder, 'dump.sql.gz' ])
        local_file = '/'.join([ env.local_folder, 'backups', env.name, env.timestamp, 'dump.sql.gz' ])

        run( 'mysqldump -u %(db_user)s -p %(db_name)s > dump.sql' % env )
        # gzip --decompress filename
        run( 'gzip --best dump.sql' )
        get( remote_file, local_file )
        run('rm -f dump.sql.gz')

@task
def migrate():
    with cd( env.remote_folder ), prefix('source venv/bin/activate'):
        run('python manage.py db upgrade')


@task
def start():
    sudo('service mysql start')
@task
def restart():
    sudo('service mysql restart')
@task
def stop():
    sudo('service mysql stop')
@task
def status():
    sudo('service mysql status')
