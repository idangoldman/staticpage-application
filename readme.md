# StaticPages

## Install
git clone

cd static-pages

### Backend
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

cp start_example.sh start.sh

### Frontend
npm install
bower install

## Run

### Backend
sh start.sh # Backend

### Frontend
gulp # Frontend