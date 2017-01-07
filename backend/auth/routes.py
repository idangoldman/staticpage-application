from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from backend import db
from backend.auth import auth
from backend.auth.forms import RegisterForm, LoginForm
from backend.models.page import Page
from backend.models.user import User


@auth.before_request
def before_request():
    if current_user.is_authenticated and not request.endpoint == 'auth.logout':
        return redirect( url_for('home') )


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # TODO: fix same site_name or email crash
        user = User(site_name=form.site_name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(email=form.email.data).first()
        page = Page(user_id=user.id)
        db.session.add(page)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('root/auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('auth.login'))
        login_user(user, form.remember_me.data)
        redirect_url = url_for('home') if not user.is_admin else url_for('root.index')
        return redirect(request.args.get('next') or redirect_url)
    return render_template('root/auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
