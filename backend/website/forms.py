from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email


class NewsletterForm( FlaskForm ):
    email = StringField('email', [ Required(), Email('Please enter your email address.') ])
    submit = SubmitField('Keep me posted!')
