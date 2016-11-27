FILE_PATH=`pwd`

# Server
export SERVER_IP=["0.0.0.0"]
export SSH_KEY_PATH="~/.ssh/..."
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export APP_SETTINGS="config.DevConfig"

# APIs
export MAILCHIMP_API_KEY=""
export MAILCHIMP_LIST_ID=""
export MAILCHIMP_USERNAME=""
export GOOGLE_ANALYTICS_ID=""
export ADDTHIS_PUBID=""


venv/bin/python application.py

