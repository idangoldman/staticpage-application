FILE_PATH=`pwd`


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export APP_SETTINGS="config.DevConfig"
export CLEANCSS_BIN="node_modules/.bin/cleancss"
export AUTOPREFIXER_BIN="${FILE_PATH}/node_modules/.bin/postcss"


export MAILCHIMP_API_KEY=""
export MAILCHIMP_LIST_ID=""
export GOOGLE_ANALYTICS_ID=""
export ADDTHIS_PUBID=""


venv/bin/python app.py

