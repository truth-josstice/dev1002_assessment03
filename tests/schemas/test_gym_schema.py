import pytest
from marshmallow import ValidationError

from init import db

def test_gym_schema_with_company_serialization(app):
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
        assert "company" in result  # Check relationship is included
        assert result["company"]["name"] == "Schema Test Company"

def test_gym_schema_company_validation(app):
    """Test that gym schema validates company_id exists"""
    from schemas.gym import gym_schema
    
    with app.app_context():
        # Try to create gym with non-existent company
        invalid_data = {
            "name": "Invalid Gym",
            "city": "Invalid City",
            "street_address": "123 Invalid St",
            "company_id": 9999  # Doesn't exist
        }
        
        with pytest.raises(ValidationError) as err:
            gym_schema.load(invalid_data, session=db.session)
        
        assert "company_id" in str(err.value)