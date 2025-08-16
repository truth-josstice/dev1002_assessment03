import os

from flask import Flask
from dotenv import load_dotenv

from init import db, bcrypt
from controllers.cli_controller import db_commands
from controllers.company_controller import company_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI") # Database URI settings
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Avoids warnings

    db.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(company_bp)

    app.json.sort_keys = False

    return app