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
@jwt_required()
def new_climb():
    # Get data from the REQUEST body
    body_data = request.get_json()
    
    new_climb = climb_input_schema.load(body_data, session=db.session)

    new_climb.user = current_user
    
    db.session.add(new_climb)
    db.session.commit()
    
    return jsonify(climb_output_schema.dump(new_climb)), 201

@climb_bp.route('/add-climbs/', methods=["POST"])
@jwt_required()
def new_climbs():
    # Get data from the REQUEST body
    body_data = request.get_json()

    new_climbs = []

    for data in body_data:
        new_climb = climb_input_schema.load(data, session=db.session)
        new_climb.user = current_user
        new_climbs.append(new_climb)
    
    db.session.add_all(new_climbs)
    db.session.commit()
    
    return jsonify(climbs_output_schema.dump(new_climbs)), 201

@climb_bp.route('/remove-climb/<int:climb_id>/', methods=["DELETE"])
@jwt_required()
def remove_a_climb(climb_id):
    """Function to DELETE a single climb belonging to the user"""
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

@climb_bp.route('/update/<int:climb_id>/', methods=["PUT", "PATCH"])
@jwt_required()
def update_a_climb_record(climb_id):
    """Function to UPDATE a single climb belonging to the user"""
    # GET statement: SELECT * FROM climbs WHERE Climb.id = climb_id
    stmt = db.select(Climb).where(Climb.id==climb_id)
    climb = db.session.scalar(stmt)

    # Check that the climb exists
    if not climb:
        return {"message": f"Climb with id {climb_id} does not exist."}, 404
    
    # Check that the current user owns the climb
    if climb.user_id != current_user.id:
        return {"message": f"{current_user.username}, you are not authorised to update this climb."}
    
    # GET JSON body data
    body_data = request.get_json()

    # Load data into climb through climb_schema
    updated_climb = climb_input_schema.load(
        body_data,
        instance = climb,
        session = db.session,
        partial = True
    )

    db.session.add(updated_climb)
    db.session.commit()

    return jsonify(climb_output_schema.dump(updated_climb))