from flask import render_template, request, redirect, url_for, flash, current_app, abort
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
import random

from backend import db, mail
from backend.auth import auth
from backend.auth.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from backend.helpers import get_a_template, get_a_stub, get_page_stub, is_phone, timed_url_safe, md5_identifier
from backend.models.page import Page
from backend.models.user import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(email = form.email.data, \
                     site_name = md5_identifier(form.email.data), \
                     password = form.password.data)
        db.session.add(user)
        db.session.commit()

        user = User.query.filter_by(email=form.email.data).first()

        template_stub = get_a_template(form.template.data)
        template_stub['user_id'] = user.id

        page = Page(**template_stub)
        db.session.add(page)
        db.session.commit()

        try:
            token = timed_url_safe().dumps(user.email, salt='email-confirm-key')
            confirm_url = url_for('auth.confirm_email', token=token, _external=True)
            text = render_template('auth/emails/confirm.txt', confirm_url=confirm_url)
            mail.send(Message("Confirmation of Successful Registration!", recipients=[user.email], body=text))
        except:
            print "Shit."

        login_user(user)

        return redirect(url_for('home'))


    with open('static/images/side-kick-sprite.svg', 'r') as svg_file:
      svg_sprite = svg_file.read()

    side_kick = get_a_stub('auth/register/side-kick')

    for field in side_kick.get('fields'):
        if field.get('id') != 'password' and form[field.get('id')].data:
            field['value'] = form[field.get('id')].data

        if field.get('id') == 'template':
            field['default'] = random.choice(('mailing_list', 'countdown_clock', 'social_icons', 'all'))

        if form[field.get('id')]:
            field['errors'] = form[field.get('id')].errors

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'on_phone': is_phone(request.user_agent),
        'page': get_page_stub('auth/register/page'),
        'side_kick': side_kick,
        'svg_sprite': svg_sprite
    }

    return render_template('auth/register.html', **payload)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or not user.verify_password(form.password.data):
            flash('Invalid email or password.', 'error')
            return redirect(url_for('auth.login'))

        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('home'))

    side_kick = get_a_stub('auth/login/side-kick')

    for field in side_kick.get('fields'):
        if field.get('id') == 'email' or field.get('id') == 'remember_me':
            if form[field.get('id')].data:
                field['value'] = form[field.get('id')].data

        if form[field.get('id')]:
            field['errors'] = form[field.get('id')].errors

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'on_phone': is_phone(request.user_agent),
        'page': get_page_stub('auth/login/page'),
        'side_kick': side_kick
    }

    return render_template('auth/login.html', **payload)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('website.welcome'))


@auth.route('/resend_confirm')
@login_required
def resend_confirm():
    token = timed_url_safe().dumps(current_user.email, salt='email-confirm-key')
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    text = render_template('auth/emails/confirm.txt', confirm_url=confirm_url)
    mail.send(Message("Confirm your email", recipients=[current_user.email], body=text))

    return redirect( request.referrer )


@auth.route('/confirm/<token>')
def confirm_email( token ):
    try:
        email = timed_url_safe().loads(token, salt = "email-confirm-key", max_age=86400) # 24hr
    except:
        abort(404)

    user = User.query.filter_by(email=email).first_or_404()
    user.email_confirmed = True

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('home'))


@auth.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        flash('Check your email.', 'notice')

        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = timed_url_safe().dumps(user.email, salt='recover-key')
            reset_url = url_for('auth.reset_password', token=token, _external=True)
            text = render_template('auth/emails/reset.txt', reset_url=reset_url)
            mail.send(Message("Reset password request", recipients=[ user.email ], body=text))

        return redirect(url_for('auth.login'))

    side_kick = get_a_stub('auth/forgot-password/side-kick')

    for field in side_kick.get('fields'):
        if field.get('id') == 'email':
            field['errors'] = form[field.get('id')].errors
            if form[field.get('id')].data:
                field['value'] = form[field.get('id')].data

    payload = {
        'form': form,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'on_phone': is_phone(request.user_agent),
        'page': get_page_stub('auth/forgot-password/page'),
        'side_kick': side_kick
    }

    return render_template('auth/forgot-password.html', **payload)


@auth.route('/reset_password/<token>', methods=["GET", "POST"])
def reset_password(token):
    try:
        email = timed_url_safe().loads(token, salt="recover-key", max_age=86400) # 24hr
    except:
        abort(404)

    form = ResetPasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = email).first_or_404()
        user.password = form.new_password.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))


    side_kick = get_a_stub('auth/reset-password/side-kick')

    for field in side_kick.get('fields'):
        if field.get('id') == 'password':
            field['errors'] = form[field.get('id')].errors

    payload = {
        'form': form,
        'token': token,
        'ga_id': current_app.config['GOOGLE_ANALYTICS_ID'],
        'on_phone': is_phone(request.user_agent),
        'page': get_page_stub('auth/reset-password/page'),
        'side_kick': side_kick
    }

    return render_template('auth/reset-password.html', **payload)
