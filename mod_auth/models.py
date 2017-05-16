from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from app.app import db
from app.models import Base

'''
User model
'''
class User(Base):
    __tablename__ = 'souvu_user'

    '''
    Email address will be the username
    '''
    email = db.Column(db.String(50), unique=True, nullable=False)

    '''
    Encrypted password for the user.    
    '''
    password_hash = db.Column(db.String(128))

    authenticated = db.Column(db.Boolean, default=False)

    admin = db.Column(db.Boolean, default=False)

    first_name = db.Column(db.String(25),  nullable=True)
    last_name = db.Column(db.String(25),  nullable=True)

    test_account = db.Column(db.Boolean, default=False)

    def check_password(self, password):
        """ Check's whether the specified password is correct """
        print("checking password")
        return check_password_hash(self.password, password)

    def is_admin(self):
        return self.admin

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)