from flask import Blueprint
from flask_login import current_user

root = Blueprint('root', __name__, url_prefix='/root')

from . import routes
