from flask import Blueprint, jsonify, request

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
    # Get login credentials from JSON body data
    body_data = request.get_json()

    # Ensure username and password are in the body data, and that body data exists
    if not body_data or "username" not in body_data or "password" not in body_data:
        return {"message": "Username and password are required"}, 400
    
    # Find user by username
    stmt = db.select(User).filter_by(username=body_data["username"])
    user = db.session.scalar(stmt)

    # Verify user exists and password is correct
    if not user or not user.check_password(body_data["password"]):
        return {"message": "Invalid username or password"}, 401

    

