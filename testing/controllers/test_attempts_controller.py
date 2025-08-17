from flask import Blueprint, jsonify, request

from init import db
from models.attempts import Attempt
from schemas.attempt_schema import attempt_schema, attempts_schema

attempt_bp = Blueprint("attempt", __name__, url_prefix="/attempts")

@attempt_bp.route('/')
def get_attempts():
    '''Function to GET multiple attempts from the database'''
    # GET statement: SELECT * FROM attempts;
    stmt = db.select(Attempt)
    attempts = db.session.scalars(stmt).all()

    if not attempts:
        return {"message": "No attempt records found."}, 404
    
    return jsonify(attempts_schema.dump(attempts))