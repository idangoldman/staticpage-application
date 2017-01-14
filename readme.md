# StaticPage

## Install
`git clone git@github.com:idangoldman/staticpage.git`

`cd staticpage`

### Backend
`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`cp flask_env.example flask_env`

### Frontend
`npm install`

`npm install -g gulp`


## Run

### Backend
`sh start.sh`


### Frontend
`gulp w`


## Deployment
`fab staging setup`

`fab staging deploy`

`fab production setup`

`fab production deploy`

### Steps of setup
- Copy and paste ssh key to github repo.
- Generate Mysql password for root and enter it couple of times.
- Edit `flask_env` file.
- Run `sudo service uwsgi restart`.
- SSL should be done by hand for now.


## Manager Commands
`python manage.py runserver`

`python manage.py db init`

`python manage.py db migrate`

`python manage.py db upgrade`


## Useful
`pip freeze > requirements.txt`

`pip-autoremove -y somepackage`
