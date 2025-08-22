import pytest
import os

from main import create_app
from init import db
from schemas import user_input_schema
from flask_jwt_extended import create_access_token


@pytest.fixture(scope='function')
def app():
    test_config = {
        'TESTING': True, # Testing is true
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db', # Use file type db for CLI function testing
        'JWT_SECRET_KEY': 'test-secret-key' # fake secret key to test validation
    }
    
    # Ensure blank or non existent database 
    if os.path.exists('test.db'):
        os.remove('test.db')

    # Initialise test app
    app = create_app(test_config=test_config)

    # 
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

    if os.path.exists('test.db'):
        os.remove('test.db')

@pytest.fixture
def runner(app):
    """Fixture for testing CLI commands"""
    from flask.testing import CliRunner
    return app.test_cli_runner()

@pytest.fixture
def client(app):
    with app.app_context():
        client = app.test_client()
        yield client
        db.session.rollback()

def create_user(app, username, email, password="TestSecurePassword1!", is_admin=False):
    """Create a user in the test DB using input schema."""
    with app.app_context():
        data = {
            "username": username,
            "email": email,
            "password": password,
            "first_name": "Name",
            "skill_level_id": 1
        }
        user = user_input_schema.load(data, session=db.session)
        db.session.add(user)
        db.session.commit()
        return user

def get_auth_header(app, user):
    """Generate an Authorization header with access token for a user."""
    with app.app_context():
        token = create_access_token(identity=user.id, expires_delta=None)
        return {"Authorization": f"Bearer {token}"}