import pytest
from sqlalchemy import inspect
from main import create_app
from init import db

def test_create_tables(runner):
    """Test flask db create command and printing output"""
    result = runner.invoke(args=['db', 'create'])
    assert result.exit_code == 0
    assert "Tables created" in result.output
    
    # Verify tables were actually created in test database
    with create_app().app_context():
        inspector = inspect(db.engine)
        assert 'companies' in inspector.get_table_names()
        assert 'users' in inspector.get_table_names()

def test_drop_tables(runner):
    """Test flask db drop commands"""
    # First create tables to drop
    runner.invoke(args=['db', 'create'])
    
    # Check the drop command occurs and prints message
    result = runner.invoke(args=['db', 'drop'])
    assert result.exit_code == 0
    assert "Tables dropped" in result.output
    
    # Verify tables were actually dropped from test database
    with create_app().app_context():
        inspector = inspect(db.engine)
        assert 'companies' not in inspector.get_table_names()

def test_seed_tables(runner):
    """Test flask db seed command"""
    # Create the tables to start with
    runner.invoke(args=['db', 'create'])
    
    # Check if the seed command occurs and prints message
    result = runner.invoke(args=['db', 'seed'])
    assert result.exit_code == 0
    assert "Tables seeded" in result.output
    
    # Verify data was actually seeded into the test database
    with create_app().app_context():
        from models.company import Company
        companies = Company.query.all()
        assert len(companies) == 2
        assert companies[0].name == "Company 1"
        assert companies[1].website == "www.website2.com"