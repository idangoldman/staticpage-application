from app import db, login_manager
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
