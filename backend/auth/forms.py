from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, ValidationError
import re

from backend.models.user import User
from backend.helpers.constants import TEMPLATE_NAMES


def unique_email(form, field):
    user = User.query.filter_by(email = field.data).first()
    if user:
        raise ValidationError('Email already exist, try another one.')

def validate_page_template(form, field):
    if not field.data in TEMPLATE_NAMES:
        raise ValidationError('Template does not exists.')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1,64), Email(), unique_email])
    password = PasswordField('Password', validators=[Required(), Length(3)])
    template = StringField('Template', validators=[validate_page_template])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Enter')

class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    submit = SubmitField('Confirm Email')

class ResetPasswordForm(FlaskForm):
    new_password = PasswordField('New Password', validators=[Required()])
    submit = SubmitField('Reset Password')
