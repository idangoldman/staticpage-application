from flask import render_template, request, redirect, url_for

from . import auth
from .forms import RegisterForm, LoginForm
from ..models import User
from .. import db


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(fullname=form.fullname.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('root/auth/register.html', form=form)


@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('root/auth/login.html', form=form)


@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))
