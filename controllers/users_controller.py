from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, current_user
from datetime import timedelta

from init import db
from models import User
from schemas import (
    user_output_schema, 
    users_output_schema,
    user_input_schema
)
from utils import admin_required

user_bp = Blueprint("user", __name__, url_prefix="/users")

@user_bp.route('/')
@jwt_required()
@admin_required
def get_users():
    '''Function to GET multiple users from the database for admin users'''

    # GET statement: SELECT * FROM users;
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()

    if not users:
        return {"message": "No user records found."}, 404
    
    return jsonify(users_output_schema.dump(users))
    
@user_bp.route('/profile/')
@jwt_required()
def get_user_profile():
    """Function to GET user profile using authorisation token"""
    return jsonify(user_output_schema.dump(current_user))

@user_bp.route('/update-profile/', methods=["PUT", "PATCH"])
@jwt_required()
def update_user_profile():
    """Function to PUT/PATCH users own profile"""
    # GET statement: SELECT * FROM users WHERE id = id;
    stmt = db.select(User).where(User.id == current_user.id)
    user = db.session.scalar(stmt)

    # User must exist so can skip any if loops
    # GET JSON body data
    body_data = request.get_json()

    # Load data into user via user_input_schema
    updated_user = user_input_schema.load(
        body_data, 
        session = db.session,
        instance = user,
        partial = True
        )
    
    db.session.add(updated_user)
    db.session.commit()

    return {
        "message": "User updated successfully.",
        "details": jsonify(user_output_schema.dump(updated_user))
    }, 200

@user_bp.route('/admin/add/', methods=["POST"])
@jwt_required()
@admin_required
def add_new_user():
    """Function to POST a new user for admin"""
    # GET JSON body data
    body_data = request.get_json()

    # Create user from body data
    new_user = user_input_schema.load(body_data, session=db.session)

    # Check if user with email already exists
    stmt = db.select(User).where(User.email==new_user.email)
    if db.session.scalar(stmt):
        return {"message": "An account with this email already exists, please login or enter a different email."}, 409
    
    # Check if user with username already exists
    stmt = db.select(User).where(User.username==new_user.username)
    if db.session.scalar(stmt):
        return {"message": f"An account with the username {new_user.username} already exists. Please choose a different username."}, 409
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_output_schema.dump(new_user))

@user_bp.route('/admin/remove/<int:user_id>', methods=["DELETE"])
@jwt_required()
@admin_required
def delete_user(user_id):
    """Function to DELETE any user for admin"""
    # GET statement: SELECT * FROM users WHERE id = user_id;
    stmt = db.select(User).where(User.id == user_id)
    user = db.session.scalar(stmt)

    # Check if user exists
    if not user:
        return {"message": f"User with id {user_id} does not exist."}, 404
    
    db.session.delete(user)
    db.session.commit()

    return {"message": f"User with id {user_id} deleted successfully."}, 200
