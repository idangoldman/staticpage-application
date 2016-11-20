from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

static_pages = Blueprint('static_pages', __name__,
                        template_folder='templates')



@static_pages.route('/', defaults={'page': 'index'})
@static_pages.route('/<page>')
def show(page):
    obj = {
        "page" : page
    }
    try:
        return render_template('pages/static.html',obj=obj)
    except TemplateNotFound:
        abort(500)