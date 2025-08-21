from flask import Blueprint, jsonify, request
from flask_jwt_extended import current_user, jwt_required

from init import db
from models import Attempt
from schemas import (
    attempt_output_schema, 
    attempts_output_schema,
    admin_attempts_schema,
    attempt_input_schema
)
from utils import admin_required

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
        "attempts": attempts_output_schema.dump(attempts)
        })

@attempt_bp.route('/<int:attempt_id>/')
@jwt_required()
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
    
    return jsonify(attempt_output_schema.dump(attempt))

@attempt_bp.route('/add-attempt/', methods=["POST"])
@jwt_required()
def add_an_attempt():
    """Function to add a single attempt using current_user"""
    # GET JSON body data
    body_data = request.get_json()

    new_attempt = attempt_input_schema.load(body_data, session=db.session)

    new_attempt.user = current_user

    db.session.add(new_attempt)
    db.session.commit()

    return jsonify(attempt_output_schema.dump(new_attempt))

@attempt_bp.route('/all/')
@jwt_required()
@admin_required
def get_all_attempts():
    stmt = db.select(Attempt)
    attempts = db.session.scalars(stmt).all()

    if not attempts:
        return {"message": "No attempt records were found."}, 404
    
    return jsonify(admin_attempts_schema.dump(attempts))