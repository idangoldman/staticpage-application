from deployment import machine, nginx, uwsgi, git, virtualenv, mysql, frontend, uploads_folder_backup
from deployment.enviroments import staging, production
from deployment.commands import setup, deploy, backup
