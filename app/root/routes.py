from flask import render_template, redirect, url_for
from flask_login import login_required

from . import root

@root.route('/')
@login_required
def index():
    return render_template('root/index.html')

@root.route('/users')
@login_required
def users():
    return redirect(url_for('root.index'))
    # return render_template('root/users.html')

@root.route('/pages')
@login_required
def pages():
    return redirect(url_for('root.index'))
    # return render_template('root/pages.html')