from flask import Blueprint
from itsdangerous import URLSafeTimedSerializer

auth = Blueprint( 'auth', __name__ )

from backend.auth import routes
