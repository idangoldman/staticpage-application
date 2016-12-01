FILE_PATH=`pwd`


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export APP_SETTINGS="config.DevConfig"
export SASS_STYLE="compressed"
export SASS_LINE_COMMENTS="False"
export AUTOPREFIXER_BIN="${FILE_PATH}/node_modules/.bin/postcss"


export MAILCHIMP_API_KEY=""
export MAILCHIMP_LIST_ID=""
export MAILCHIMP_USERNAME=""
export GOOGLE_ANALYTICS_ID=""
export ADDTHIS_PUBID=""


venv/bin/python app.py

