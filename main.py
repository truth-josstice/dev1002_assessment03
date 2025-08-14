import os

from flask import Flask
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

from init import db
from controllers.cli_controller import db_commands

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI") # Database URI settings
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Avoids warnings

    db.init_app(app)
    bcrypt = Bcrypt(app)

    app.register_blueprint(db_commands)

    app.json.sort_keys = False

    return app