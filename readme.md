# StaticPage

## Install
git clone

cd staticpage

### Backend
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

cp flask_env.example flask_env

### Frontend
npm install

npm install -g gulp

## Run

### Backend
sh start.sh

### Frontend
gulp

### Manager Commands
python manage.py runserver

python manage.py db init

python manage.py db migrate

python manage.py db upgrade


### Useful
pip freeze > requirements.txt

pip-autoremove -y somepackage
