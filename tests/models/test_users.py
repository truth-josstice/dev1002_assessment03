def test_user_creation(app):
    """Test we can create a user based on the user model"""
    from models.users import User
    with app.app_context():
        user = User(
            username="simpleuser",
            email="simple@test.com",
            first_name="Simple",
            climbing_ability="Beginner",
            password="securepassword123"
        )
        assert user.username == "simpleuser"
        assert user.email == "simple@test.com"