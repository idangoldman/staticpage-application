FILE_PATH=`pwd`

# Server
export SERVER_IP=["0.0.0.0"]
export SSH_KEY_PATH="~/.ssh/..."
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export APP_SETTINGS="config.DevConfig"
export GIT_REPO_PATH="git@github.com:idanm/static-pages.git"

# Webassets
export SASS_STYLE="compressed"
export SASS_LINE_COMMENTS="False"
export AUTOPREFIXER_BIN="${FILE_PATH}/node_modules/.bin/postcss"

# APIs
export MAILCHIMP_API_KEY=""
export MAILCHIMP_LIST_ID=""
export GOOGLE_ANALYTICS_ID=""
export ADDTHIS_PUBID=""


venv/bin/python app.py

