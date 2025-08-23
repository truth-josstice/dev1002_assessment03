import pytest
from sqlalchemy.exc import IntegrityError

from init import db
from models import Gym

def test_gym_schema_serialization(app):
    """Test gym schema includes company data when serialized"""
    from models import Company, Gym
    from schemas import gym_schema
    
    with app.app_context():
        # Create test data
        company = Company(name="Schema Test Company", website="www.schema.com")
        db.session.add(company)
        db.session.commit()
        
        gym = Gym(
            company_id=company.id,
            name="Schema Test Gym",
            city="Schema City",
            street_address="123 Schema St"
        )
        db.session.add(gym)
        db.session.commit()
        
        # Serialize
        result = gym_schema.dump(gym)
        
        # Test the serialized output
        assert result["name"] == "Schema Test Gym"
        assert result["company_id"] == 1