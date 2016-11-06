from wtforms import form, fields,Form,TextField
from flask_admin.contrib.pymongo import ModelView

class UserForm(Form):
    name = TextField('Name')
    email = TextField('Email')

class UserView(ModelView):
    column_list = ('name', 'email')
    form = UserForm