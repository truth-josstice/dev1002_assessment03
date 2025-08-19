from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Variables to import into main.py for activation
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt_manager = JWTManager()

# JWT user callback functionality
