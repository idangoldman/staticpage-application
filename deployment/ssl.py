from fabric.api import *
from fabric.contrib import files


@task
def setup():
    sudo('openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048')
    update_conf_file()

    if env.name == 'staging':
        fake_certificate()
    elif env.name == 'production':
        letsencrypt()


def fake_certificate():
    prompts_dict = {
        'Country Name (2 letter code) [AU]:': 'IS',
        'State or Province Name (full name) [Some-State]:': 'Israel',
        'Locality Name (eg, city) []:': 'Tel Aviv',
        'Organization Name (eg, company) [Internet Widgits Pty Ltd]:': env.company_name,
        'Organizational Unit Name (eg, section) []:': env.company_name,
        'Common Name (e.g. server FQDN or YOUR name) []:': env.domain,
        'Email Address []:': env.email
    }

    with settings( prompts = prompts_dict ):
        sudo( 'openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout %(ssl_key_path)s -out %(ssl_crt_path)s' % env )


def letsencrypt():
    # print "not created yet."
    sudo( 'letsencrypt certonly -a webroot --webroot-path=%(remote_folder)s -d %(domain)s -d www.%(domain)s' % env )


@task
def update_conf_file():
    kwargs = {
        'filename': 'ssl.jnj',
        'destination': '/etc/nginx/snippets/ssl.conf',
        'template_dir': 'deployment/templates',
        'context': {
            'ssl_crt_path': env.ssl_crt_path,
            'ssl_key_path': env.ssl_key_path
        },
        'use_jinja': True,
        'use_sudo': True,
        'backup': False
    }

    files.upload_template( **kwargs )
