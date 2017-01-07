from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user

from backend.root import root


@root.before_request
def before_request():
    if current_user.is_anonymous:
        return abort(401)
    elif current_user.is_authenticated and not current_user.is_admin:
        return redirect(url_for('home'))


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
