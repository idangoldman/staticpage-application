from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True)
    site_name = db.Column('site_name', db.String(64), nullable=False, unique=True, index=True)
    email = db.Column('email', db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column('password_hash', db.String(128), nullable=False)
    is_admin = db.Column('is_admin', db.Boolean, default=False)
    joined_at = db.Column('joined_at', db.DateTime(), default=datetime.utcnow)

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

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column('created_at', db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime(), default=datetime.utcnow)

    file_type = db.Column('file_type', db.String(16), nullable=False, default='welcome')
    file_name = db.Column('file_name', db.String(128), default='index')

    content_logo = db.Column('content_logo', db.String(128))
    content_title = db.Column('content_title', db.Text())
    content_sub_title = db.Column('content_sub_title', db.Text())
    content_description = db.Column('content_description', db.Text())

    design_background_image = db.Column('design_background_image', db.String(128))
    design_background_color = db.Column('design_background_color', db.String(8))
    design_background_repeat = db.Column('design_background_repeat', db.String(16))
    design_font_family = db.Column('design_font_family', db.String(128))
    design_base_font_size = db.Column('design_base_font_size', db.String(8))
    design_font_color = db.Column('design_font_color', db.String(8))
    design_content_alignment = db.Column('design_content_alignment', db.String(8))
    design_content_direction = db.Column('design_content_direction', db.String(3))
    design_additional_styles = db.Column('design_additional_styles', db.Text())

    search_results_title = db.Column('search_results_title', db.Text())
    search_results_description = db.Column('search_results_description', db.Text())
