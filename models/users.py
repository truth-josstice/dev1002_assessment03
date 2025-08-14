from init import db

from sqlalchemy.ext.declarative import declarative_base
from flask_bcrypt import Bcrypt

class User(db.model):
    '''
    User Table Model with constraints
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False) # Secure storage of passwords