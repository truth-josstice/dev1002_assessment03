import os

from flask import Flask
from dotenv import load_dotenv

from init import db, bcrypt, jwt_manager
from utils import register_error_handlers
from controllers import (
    db_commands,
    auth_bp,
    company_bp,
    gym_bp,
    climb_bp,
    attempt_bp,
    gym_rating_bp,
    user_bp
)

load_dotenv()

def create_app() -> Flask:
    """Creates and configures the Flask application with database and blueprints."""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI") # Database URI settings
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Disables modification tracking to avoid compatability issues

    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY") # Retrieves random SECRET KEY from .env

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt_manager.init_app(app)

    # Register blueprints from a list with a for loop instead of individually
    blueprints = [
        db_commands, 
        company_bp, 
        gym_bp, 
        climb_bp, 
        attempt_bp, 
        gym_rating_bp,
        user_bp,
        auth_bp]
    
    for bp in blueprints:
        app.register_blueprint(bp)

    register_error_handlers(app)

    # removed for DRY coding
    # app.register_blueprint(db_commands)
    # app.register_blueprint(company_bp)
    # app.register_blueprint(gym_bp)
    # app.register_blueprint(climb_bp)

    app.json.sort_keys = False

    return app