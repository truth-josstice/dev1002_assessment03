from init import db, bcrypt

from sqlalchemy.ext.declarative import declarative_base

class User(db.model):
    '''
    User Table Model with constraints
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False) # Secure storage of passwords
    email = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    climbing_ability = db.Column(db.string, nullable=False)

    @property
    def password(self):
        raise AttrubuteError("Password is write-only (cannot be read)")

    @password.setter
    def password(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)