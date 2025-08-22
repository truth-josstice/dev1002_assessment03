from init import db

from models import User, SkillLevel

def test_user_creation(app):
    """Test we can create a user based on the user model"""
    
    with app.app_context():
        skill = SkillLevel(
            id = 4,
            level = "Beginner",
            description = "testdescription"
        )
        db.session.add(skill)
        db.session.commit()

        user = User(
            username="simpleuser",
            email="simple@test.com",
            first_name="Simple",
            skill_level_id=skill.id,
            password="Test123!"  # Will be hashed by model
        )
        assert user.username == "simpleuser"
        assert user.email == "simple@test.com"