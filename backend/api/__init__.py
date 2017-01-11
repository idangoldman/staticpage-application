from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from backend.api import routes, errors
