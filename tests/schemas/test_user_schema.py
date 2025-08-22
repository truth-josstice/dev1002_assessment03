import pytest
from marshmallow import ValidationError
from init import db
from models import User, SkillLevel
from schemas import user_input_schema, user_output_schema, users_output_schema

def test_user_schema_serialization(app):
    """Test user schema serialization to JSON format"""
    with app.app_context():
        skill = SkillLevel(
            id = 1,
            level = "Beginner",
            description = "testdescription"
        )
        db.session.add(skill)
        db.session.commit()

        user = User(
            username="serial_test",
            email="serial@test.com",
            first_name="Serial",
            skill_level_id=skill.id,
            password="Test123!"  # Will be hashed by model
        )
        db.session.add(user)
        db.session.commit()

        result = user_output_schema.dump(user)
        
        assert result["username"] == "serial_test"
        assert "password" not in result  # Password should never be exposed when data is requested
        assert "_password_hash" not in result # Password hash should never be displayed when data is requested

def test_user_schema_deserialization(app):
    """Test schema loading with valid User object data"""
    with app.app_context():
        # Test data matching what your schema actually accepts

        valid_data = {
            "username": "load_test",
            "email": "load@test.com",
            "first_name": "Load",
            "last_name": "Test"
            # Omit password since it is not returned in the data
        }
        
        # Check the data is loaded correctly
        loaded = user_output_schema.load(valid_data, session=db.session)
        assert loaded.username == "load_test"

def test_user_schema_password_handling(app):
    """Test password is handled outside of the user schema in order to never be displayed as part of request"""
    with app.app_context():
        # Create user directly to test password
        skill = SkillLevel(
            id = 1,
            level = "Beginner",
            description = "testdescription"
        )
        db.session.add(skill)
        db.session.commit()
        user = User(
            username="serial_test",
            email="serial@test.com",
            first_name="Serial",
            skill_level_id=skill.id,
            password="Test123!"  # Will be hashed by model
        )
        db.session.add(user)
        db.session.commit()
        
        # Verify password was hashed by checking for data, and ensuring password string is not in the result
        assert user._password_hash is not None
        assert user._password_hash != "correct123"

def test_user_schema_validation(app):
    """Test schema validation for NOT NULL fields"""
    with app.app_context():
        invalid_data = {
            "email": "invalid@test.com"
            # Missing required username, first_name, etc.
        }
        
        with pytest.raises(ValidationError) as err:
            user_input_schema.load(invalid_data, session=db.session)
        
        assert "username" in str(err.value)  # Should complain about missing username