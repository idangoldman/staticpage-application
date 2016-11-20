from flask_admin import  BaseView, expose
from flask_pymongo import PyMongo
from flask import current_app as app
from flask_admin.contrib.mongoengine import ModelView

class adminPage(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/page.html')


class UserView(ModelView):
    column_filters = ['name']

    column_searchable_list = ('name', 'password')

    form_ajax_refs = {

    }