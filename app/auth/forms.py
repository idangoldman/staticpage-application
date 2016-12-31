from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp


class RegisterForm(FlaskForm):
    site_name = StringField('Site Name', validators=[Required(), Regexp(r'^[a-zA-Z0-9_-]+$', message='Site Name can only use a-zA-Z0-9-_ characters'), Length(3,64)])
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[Required(), Length(8)])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Enter')
