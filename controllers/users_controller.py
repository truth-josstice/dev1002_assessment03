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
    body_data