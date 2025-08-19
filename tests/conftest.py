import pytest
from main import create_app
from init import db


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    """Fixture for testing CLI commands"""
    from flask.testing import CliRunner
    return app.test_cli_runner()

@pytest.fixture
def client(app):
    with app.app_context():
        yield app.test_client()
        db.session.rollback()