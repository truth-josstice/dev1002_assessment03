from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Variables to import into main.py for activation
db = SQLAlchemy()
bcrypt = Bcrypt()