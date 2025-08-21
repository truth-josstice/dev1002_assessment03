from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, current_user
from datetime import timedelta

from init import db
from models.user import User
from schemas.user import user_schema, users_schema

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
    
@user_bp.route('/profile/')
@jwt_required()
def get_user_profile():
    return jsonify(user_schema.dump(current_user))

