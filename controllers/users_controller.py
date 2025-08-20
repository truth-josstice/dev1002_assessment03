from flask import Blueprint, jsonify, request, session
from flask_jwt_extended import create_access_token, jwt_required, current_user
from datetime import timedelta

from init import db
from models.users import User
from schemas.user_schema import user_schema, users_schema

user_bp = Blueprint("user", __name__, url_prefix="/users")

@user_bp.route('/')
def get_users():
    '''Function to GET multiple users from the database'''
    # GET statement: SELECT * FROM users;
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()

    if not users:
        return {"message": "No user records found."}, 404
    
    return jsonify(users_schema.dump(users))

@user_bp.route('/login/', methods=["POST"])
def user_login():
    """
    On successful login, the frontend should: 
    1. Store the current user token
    2. Redirect to the user profile with:
        - Authorization: Bearer <token>
    """
    
    # Get login credentials from JSON body data
    body_data = request.get_json()

    # IF username and password are in the body data, or the body data does not exist, send a message
    if not body_data or "username" not in body_data or "password" not in body_data:
        return {"message": "Username and password are required"}, 400
    
    # Find user by username
    stmt = db.select(User).filter_by(username=body_data["username"])
    user = db.session.scalar(stmt)

    # IF the user or password are not correct, send a message
    if not user or not user.check_password(body_data["password"]):
        return {"message": "Invalid username or password"}, 401
    
    # Create an access token for the user, sets it to logout automatically after 2 hours
    token = create_access_token(
        identity=str(user.id),
        expires_delta=timedelta(hours=2)
    )
    

    # Return the token and redirect to the user's profile
    return {
        "token": token,
        "redirect": {
            "url": "/profile/",
            "method": "GET",
            "headers": {
                "Authorization": f"Bearer {token}"
            }
        }
    }
    
@user_bp.route('/profile/')
@jwt_required()
def get_user_profile():
    return jsonify(user_schema.dump(current_user))