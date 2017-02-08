from fabric.api import *

@task
def user_folder_backup():
    with cd( env.remote_folder ):
        remote_file = '/'.join([ env.remote_folder, 'user_data.tar.gz' ])
        local_file = '/'.join([ env.local_folder, 'backups', env.name, env.timestamp, 'user_data.tar.gz' ])

        # unzip tar -zxvf user_data.tar.gz
        run('tar -zcvf user_data.tar.gz user_data/')
        get( remote_file, local_file )
        run('rm -f user_data.tar.gz')
