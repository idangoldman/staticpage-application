from fabric.api import *
from fabric.contrib import files


@task
def setup():
    sudo('apt-get install -y mysql-server')
    sudo('service mysql start')

    prompts_dict = {
        'Enter current password for root (enter for none): ': '',
        'Set root password? [Y/n] ': 'n',
        'Press y|Y for Yes, any other key for No: ': 'No',
        'Remove anonymous users? [Y/n] ': 'Y',
        'Disallow root login remotely? [Y/n] ': 'n',
        'Remove test database and access to it? [Y/n] ': 'Y',
        'Reload privilege tables now? [Y/n] ': 'Y'
    }

    with settings(prompts = prompts_dict):
        sudo('mysql_secure_installation')

    with settings(prompts = prompts_dict):
        sudo('mysql_secure_installation')
    run('mysql -u root -p -e "CREATE DATABASE staticpage;"')
