from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, ValidationError

from backend.models.user import User


def unique_site_name( form, field ):
    user = User.query.filter_by( site_name = field.data ).first()
    if user:
        raise ValidationError( 'Site name already exist, try another one.' )


def unique_email( form, field ):
    user = User.query.filter_by( email = field.data ).first()
    if user:
        raise ValidationError( 'Email already exist, try another one.' )


class RegisterForm( FlaskForm ):
    site_name = StringField('Site Name', validators=[ Required(), \
                            Regexp( r'^[a-zA-Z0-9_-]+$', \
                                    message = 'Site Name can only use a-zA-Z0-9-_ characters' ), \
                            Length( 3,64 ), \
                            unique_site_name ] )
    email = StringField('Email', validators=[ Required(), Length(1,64), Email(), unique_email ])
    password = PasswordField('Password', validators=[ Required(), Length(3) ])
    submit = SubmitField('Register')


class LoginForm( FlaskForm ):
    email = StringField( 'Email', validators=[ Required(), Length(1, 64), Email() ] )
    password = PasswordField( 'Password', validators=[ Required() ] )
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Enter')

class ForgotPasswordForm( FlaskForm ):
    email = StringField( 'Email', validators=[ Required(), Length(1, 64), Email() ] )
    submit = SubmitField('Confirm Email')

class ResetPasswordForm( FlaskForm ):
    new_password = PasswordField( 'New Password', validators=[ Required() ] )
    submit = SubmitField('Reset Password')
