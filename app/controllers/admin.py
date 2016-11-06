from flask.ext.admin import  BaseView, expose


class adminPage(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/page.html')