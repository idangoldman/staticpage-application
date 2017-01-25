from flask import Blueprint

website = Blueprint( 'website', __name__ )

from backend.website import routes
