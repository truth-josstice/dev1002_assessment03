import pytest

from marshmallow import ValidationError
from init import db
from models import Company
from schemas import company_schema, companies_schema

def test_company_schema_serialization(app):
    """Test company schema serialization to JSON format"""
    # Create the company
    with app.app_context():
        company = Company(
            name="serial_test",
            website="http://www.company.com",
            )
        db.session.add(company)
        db.session.commit()

        # Create JSON serialized output
        result = company_schema.dump(company)
        
        # Check for the correct output fields and data
        assert result["name"] == "serial_test"
        assert "http" in result["website"]

def test_company_schema_deserialization(app):
    """Test schema loading with valid Company object data"""
    
    with app.app_context():
        # Create valid data for serialization
        valid_data = {
            "name": "load_test",
            "website": "http://www.load.com"
        }
        
        # Check the data is loaded correctly
        loaded = company_schema.load(valid_data, session=db.session)
        assert loaded.name == "load_test"
        assert loaded.website == "http://www.load.com"

def test_company_schema_validation(app):
    """Test schema validation for NOT NULL fields"""
    
    # Create company with invalid data (null) for name field
    with app.app_context():
        invalid_data = {
            "website": "http://www.websiteonly.com"
            # Missing required name field
        }
        
        # Check for validation error
        with pytest.raises(ValidationError) as err:
            company_schema.load(invalid_data, session=db.session)
        
        # Ensure validation error is referring to null "name" field
        assert "name" in str(err.value)