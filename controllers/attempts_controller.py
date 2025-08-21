from flask import Blueprint, jsonify, request
from flask_jwt_extended import current_user, jwt_required

from init import db
from models import Attempt
from schemas import attempt_schema, attempts_schema

attempt_bp = Blueprint("attempt", __name__, url_prefix="/attempts")

@attempt_bp.route('/')
@jwt_required()
def get_user_attempts():
    '''Function to GET multiple attempts from the database'''
    # GET statement: SELECT * FROM attempts WHERE current_user.id == attempt.user_id;
    stmt = db.select(Attempt).where(current_user.id == Attempt.user_id)
    attempts = db.session.scalars(stmt).all()

    if not attempts:
        return {"message": "No attempt records found."}, 404
    
    return jsonify({
        "username": current_user.username, 
        "attempts": attempts_schema.dump(attempts)
        })

@attempt_bp.route('/<int:attempt_id>/')
def get_a_single_attempt(attempt_id):
    """Function to get a single attempt record from the database"""
    # GET statement: SELECT * FROM attempts WHERE current_user.id == attempt.user_id AND Attempt.id == attempt_id;
    stmt = db.select(Attempt).where(
        (current_user.id == Attempt.user_id) & 
        (attempt_id == Attempt.id)
        )
    attempt = db.session.scalar(stmt)

    if not attempt:
        return {"message": "No attempt record found."}
    
    return jsonify(attempt_schema.dump(attempt))