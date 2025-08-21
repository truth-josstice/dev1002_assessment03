from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, current_user
from datetime import timedelta

from init import db
from models import User
from schemas import user_schema, users_schema
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
    
    return jsonify(users_schema.dump(users))
    
@user_bp.route('/profile/')
@jwt_required()
def get_user_profile():
    """Function to GET user profile using authorisation token"""
    return jsonify(user_schema.dump(current_user))

