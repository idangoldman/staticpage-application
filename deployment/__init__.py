from fabric.api import *

@task
def uploads_folder_backup():
    with cd( env.remote_folder ):
        remote_file = '/'.join([ env.remote_folder, 'uploads.tar.gz' ])
        local_file = '/'.join([ env.local_folder, 'backups', env.name, env.timestamp, 'uploads.tar.gz' ])

        # unzip tar -zxvf uploads.tar.gz
        run('tar -zcvf uploads.tar.gz uploads/')
        get( remote_file, local_file )
        run('rm -f uploads.tar.gz')
