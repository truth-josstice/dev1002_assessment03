from flask import Blueprint, jsonify, request
from flask_jwt_extended import current_user, jwt_required

from init import db
from models.attempts import Attempt
from schemas.attempt_schema import attempt_schema, attempts_schema

attempt_bp = Blueprint("attempt", __name__, url_prefix="/attempts")

@attempt_bp.route('/')
@jwt_required()
def get_user_attempts():
    '''Function to GET multiple attempts from the database'''
    # GET statement: SELECT * FROM attempts WHERE current_user and attempt.user_id match;
    stmt = db.select(Attempt).where(current_user.id == Attempt.user_id)
    attempts = db.session.scalars(stmt).all()

    if not attempts:
        return {"message": "No attempt records found."}, 404
    
    return jsonify({
        "username": current_user.username, 
        "attempts": attempts_schema.dump(attempts)
        })

