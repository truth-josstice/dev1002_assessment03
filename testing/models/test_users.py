from init import db, bcrypt

class User(db.Model):
    '''
    User Table Model with constraints
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False) # Secure storage of passwords
    email = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    climbing_ability = db.Column(db.String, nullable=False)

    climbs = db.relationship("Climb", back_populates="user")
    gym_rating = db.relationship("GymRating", back_populates="user")
    attempt = db.relationship("Attempt", back_populates="user")

    # set password property and raise error if reading is requested
    @property
    def password(self):
        raise AttrubuteError("Password is write-only (cannot be read)")

    # set password attribute to be encrypted for storage in the database
    @password.setter
    def password(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # checks plain text input against encrypted hash stored in database
    def check_password(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)