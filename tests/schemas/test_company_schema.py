import pytest

from marshmallow import ValidationError
from init import db
from models import Company
from schemas import company_schema, companies_schema

def test_company_schema_serialization(app):
    """Test company schema serialization to JSON format"""
    with app.app_context():
        company = Company(
            name="serial_test",
            website="www.company.com",
            )
        db.session.add(company)
        db.session.commit()

        result = company_schema.dump(company)
        
        assert result["name"] == "serial_test"
        assert "www" in result["website"]

def test_company_schema_deserialization(app):
    """Test schema loading with valid Company object data"""
    with app.app_context():
        # Test data matching what your schema actually accepts
        valid_data = {
            "name": "load_test",
            "website": "www.load.com"
        }
        
        # Check the data is loaded correctly
        loaded = company_schema.load(valid_data, session=db.session)
        assert loaded.name == "load_test"
        assert loaded.website == "www.load.com"

def test_company_schema_validation(app):
    """Test schema validation for NOT NULL fields"""
    with app.app_context():
        invalid_data = {
            "website": "www.websiteonly.com"
            # Missing required name field
        }
        
        with pytest.raises(ValidationError) as err:
            company_schema.load(invalid_data, session=db.session)
        
        assert "name" in str(err.value)  # Should complain about missing companyname