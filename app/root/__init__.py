from flask import Blueprint, abort, url_for, redirect
from flask_login import current_user

root = Blueprint('root', __name__, url_prefix='/root')

from . import routes

@root.before_request
def before_request():
    if current_user.is_anonymous:
        return abort(401)
    elif current_user.is_authenticated and not current_user.is_admin:
        return redirect(url_for('home'))
