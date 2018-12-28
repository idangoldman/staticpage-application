from flask import jsonify
from backend.api import api


def bad_request(message):
    response = jsonify({'code': 400, 'status': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'code': 401, 'status': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'code': 403, 'status': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def not_found(message):
    response = jsonify({'code': 404, 'status': 'not found', 'message': message})
    response.status_code = 404
    return response


@api.errorhandler(404)
def not_found_handler(e):
    return not_found('resource not found')
