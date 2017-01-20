from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import Required, Email


class NewsletterForm( FlaskForm ):
    email = StringField("email", [ Required(), Email("Please enter your email address.") ])
