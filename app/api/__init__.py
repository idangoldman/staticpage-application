from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from . import routes, errors

# @api.before_request
# def before_api_request():
#     if request.json is None:
#         return errors.bad_request('Invalid JSON in body.')
#     token = request.json.get('token')
#     if not token:
#         return errors.unauthorized('Authentication token not provided.')
#     user = User.validate_api_token(token)
#     if not user:
#         return errors.unauthorized('Invalid authentication token.')
#     g.current_user = user