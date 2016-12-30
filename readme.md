# StaticPages

## Install
git clone

cd static-pages

### Backend
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

cp .env_flask.example .env_flask

### Frontend
npm install

npm install -g gulp bower

bower install

## Run

### Backend
sh start.sh

### Frontend
gulp

### Migrate
python migrate.py db init

python migrate.py db migrate

python migrate.py db upgrade
