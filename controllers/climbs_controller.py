from flask import Blueprint, jsonify, request
from flask_jwt_extended import current_user, jwt_required

from init import db
from models import Climb
from schemas import (
    climb_input_schema,
    climb_output_schema,
    climbs_output_schema
    )

climb_bp = Blueprint("climb", __name__, url_prefix="/climbs")

@climb_bp.route('/')
def get_climbs():
    '''Function to GET multiple climbs from the database. 
    All visitors to site can use this function.'''
    # GET statement: SELECT * FROM climbs;
    stmt = db.select(Climb)
    climbs = db.session.scalars(stmt).all()

    if not climbs:
        return {"message": "No climb records found."}, 404
    
    return jsonify(climbs_output_schema.dump(climbs))

@climb_bp.route('/add-climb/', methods=["POST"])
def new_climb():
    # Get data from the REQUEST body
    body_data = request.get_json()
    
    new_climb = climb_input_schema.load(body_data, session=db.session)
    
    db.session.add(new_climb)
    db.session.commit()
    
    return jsonify(climb_output_schema.dump(new_climb)), 201

@climb_bp.route('/add-climbs/', methods=["POST"])
def new_climbs():
    # Get data from the REQUEST body
    body_data = request.get_json()

    new_climbs = []

    for data in body_data:
        new_climb = climb_input_schema.load(data, session=db.session)
        new_climbs.append(new_climb)
    
    db.session.add_all(new_climbs)
    db.session.commit()
    
    return jsonify(climbs_output_schema.dump(new_climbs)), 201

@climb_bp.route('/remove-climb/<int:climb_id>/', methods=["DELETE"])
@jwt_required()
def remove_a_climb(climb_id):
    #GET statement: SELECT * FROM climbs WHERE Climb.id == climb_id;
    stmt = db.select(Climb).where(Climb.id == climb_id)
    climb = db.session.scalar(stmt)
  
    # Check that the climb exists
    if not climb:
        return {"message": f"No climb was found with id {climb_id}."}, 404
    
    # Check that the current user owns the climb
    if climb.user_id != current_user.id:
        return {"message": f"{current_user.username}, you are not authorised to delete this climb."}

    # If both checks pass delete the climb
    db.session.delete(climb)
    db.session.commit()
    return {"message": f"Climb with id {climb_id} has been removed successfully."},200