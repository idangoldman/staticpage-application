from flask import Blueprint, abort, url_for, redirect
from flask_login import current_user

root = Blueprint('root', __name__, url_prefix='/root')

from . import routes
