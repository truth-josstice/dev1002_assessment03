from init import db

def test_get_users_empty(client):
    """Test GET /users with no users (empty DB) returns error and correct status code"""
    response = client.get('/users/')
    assert response.status_code == 404
    assert b"No user records found" in response.data

def test_get_users_with_data(client, app):
    """Test GET /users with existing users returns correct responses and status code"""
    # Add test user directly with discrete paramaters
    with app.app_context():
        from models.users import User
        test_user = User(
            username="testuser",
            email="test@test.com",
            first_name="Test",
            climbing_ability="5.10a",
            password="123"
        )
        db.session.add(test_user)
        db.session.commit()

    # Test the endpoint
    response = client.get('/users/')
    assert response.status_code == 200
    assert b"testuser" in response.data
    assert b"test@test.com" in response.data