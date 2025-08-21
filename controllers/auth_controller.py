from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta

from init import db
from models import User
from schemas import (
    UserSchema, 
    UserInputSchema, 
    user_schema, 
    users_schema, 
    user_input_schema
)

auth_bp = Blueprint("auth", __name__, url_prefix="/")

@auth_bp.route('/login', methods=["POST"])
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
        expires_delta=timedelta(minutes=15)
    )
    

    # Return the token and redirect to the user's profile
    return jsonify({
        "token": token,
        "redirect": {
            "url": "/profile/",
            "method": "GET",
            "headers": {
                "Authorization": f"Bearer {token}"
            }
        }
    })

@auth_bp.route('/register', methods=["POST"])
def register_user():
    # GET JSON body data
    body_data = request.get_json()

    # Create new user using schema
    new_user = user_input_schema.load(body_data, session=db.session)

    # Check if user with email already exists
    stmt = db.select(User).where(User.email==new_user.email)
    if db.session.scalar(stmt):
        return {"message": "An account with this email already exists, please login or enter a different email."}, 409
    
    stmt = db.select(User).where(User.username==new_user.username)
    if db.session.scalar(stmt):
        return {"message": f"An account with the username {new_user.username} already exists. Please choose a different username."}, 409
    
    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=new_user.id)

    return {
        "message": "User created successfully.",
        "access_token": access_token,
        "user": user_schema.dump(new_user)
        }, 201

@auth_bp.route('/logout')
@jwt_required()
def user_logout():
    """
    Logout endpoint.
    Note: The access tokens in this app have a short lifespan of 15 minutes.
    At this stage of development I don't have refresh tokens so nothing is blacklisted.
    Future development would include refresh tokens and blacklist them on logout.
    """
    return {"message": "Successfully logged out, access token will expire shortly."}, 200