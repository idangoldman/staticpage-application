from flask import render_template

from . import root

@root.route('/')
def index():
    return render_template('root/index.html')

@root.route('/users')
def users():
    return render_template('root/users.html')

@root.route('/pages')
def pages():
    return render_template('root/pages.html')