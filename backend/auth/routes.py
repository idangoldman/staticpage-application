from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user

from backend import db
from backend.auth import auth
from backend.auth.forms import RegisterForm, LoginForm
from backend.helpers import get_a_stub, get_page_stub, is_phone
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
        user = User( site_name = form.site_name.data, \
                     email = form.email.data, \
                     password = form.password.data )
        db.session.add( user )
        db.session.commit()

        user = User.query.filter_by(email=form.email.data).first()
        page = Page( user_id = user.id )
        db.session.add( page )
        db.session.commit()

        return redirect( url_for('auth.login') )

    side_kick = get_a_stub('auth/register/side-kick')

    for field in side_kick.get('fields'):
        if field.get('id') == 'email' or field.get('id') == 'site_name':
            if form[ field.get('id') ].data:
                field['value'] = form[ field.get('id') ].data

        if form[ field.get('id') ]:
            field['errors'] = form[ field.get('id') ].errors

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'on_phone': is_phone( request.user_agent ),
        'page': get_page_stub('auth/register/page'),
        'side_kick': side_kick
    }

    return render_template( 'auth/register.html', **payload )


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by( email=form.email.data ).first()

        if user is None or not user.verify_password( form.password.data ):
            flash('Invalid email or password.')
            return redirect( url_for('auth.login') )

        login_user( user, form.remember_me.data )
        return redirect( request.args.get('next') or url_for('home') )

    side_kick = get_a_stub('auth/login/side-kick')

    for field in side_kick.get('fields'):
        if field.get('id') == 'email' or field.get('id') == 'site_name':
            if form[ field.get('id') ].data:
                field['value'] = form[ field.get('id') ].data

        if form[ field.get('id') ]:
            field['errors'] = form[ field.get('id') ].errors

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'on_phone': is_phone( request.user_agent ),
        'page': get_page_stub('auth/login/page'),
        'side_kick': side_kick
    }

    return render_template( 'auth/login.html', **payload )


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect( url_for('website.welcome') )
