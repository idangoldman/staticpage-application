from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    joined_at = db.Column(db.DateTime(), default=datetime.utcnow)

    pages = db.relationship('Page', lazy='dynamic', backref='creator')


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    file_type = db.Column(db.String(16), nullable=False, default='welcome')
    file_name = db.Column(db.String(128), default='index')

    content_logo = db.Column(db.String(128))
    content_title = db.Column(db.Text())
    content_sub_title = db.Column(db.Text())
    content_description = db.Column(db.Text())

    design_background_image = db.Column(db.String(128))
    design_background_color = db.Column(db.String(8))
    design_background_repeat = db.Column(db.String(16))
    design_font_family = db.Column(db.String(128))
    design_base_font_size = db.Column(db.String(8))
    design_font_color = db.Column(db.String(8))
    design_content_alignment = db.Column(db.String(8))
    design_content_direction = db.Column(db.String(3))
    design_additional_styles = db.Column(db.Text())

    search_results_title = db.Column(db.Text())
    search_results_description = db.Column(db.Text())
