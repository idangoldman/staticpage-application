# StaticPage

## Install
`git clone git@github.com:idangoldman/staticpage.git`

`cd staticpage`

### Backend
`pipenv install`

`cp .env.example .env`

### Frontend
`npm install`

`npm install -g gulp`


## Run

### Backend
`pipenv run sh start.sh`


### Frontend
`gulp w`


## Deployment
heroku create
git push heroku master
heroku ps
heroku ps:scale web=1
heroku open
heroku logs --tail
heroku local web

Procfile

### Steps of setup

## Manager Commands
`python manage.py runserver`

`python manage.py db init`

`python manage.py db migrate`

`python manage.py db upgrade`


## Useful
`pipenv` - for all the python env package management

`ncu` - check npm package updates

`ncu -u` - upgrade

`ncu -a` - upgrade core

`cd ~/public_html; php -S localhost:8000` - simple php server

## heroku
`heroku repo:purge_cache -a appname` - clear cache
