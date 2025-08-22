from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload
from flask_jwt_extended import jwt_required


from init import db
from models import Gym
from utils import admin_required

from schemas import (
    climbs_output_schema, 
    gym_schema, 
    gyms_schema
)

gym_bp = Blueprint("gym", __name__, url_prefix="/gyms")

@gym_bp.route('/')
def get_gyms():
    '''Function to GET multiple gyms from the database'''
    # GET statement: SELECT * FROM gyms;
    stmt = db.select(Gym)
    gyms = db.session.scalars(stmt).all()

    if not gyms:
        return {"message": "No gym records found."}, 404
    
    return jsonify(gyms_schema.dump(gyms)), 200

@gym_bp.route('/<int:gym_id>/')
def get_a_gym(gym_id):
    '''Function to get a single gym record from the database'''
    # GET statements: SELECT * FROM gyms WHERE Gym.id == gym_id;
    stmt = db.select(Gym).where(Gym.id==gym_id)
    gym = db.session.scalar(stmt)

    if not gym:
        return {"message": f"No gym with id {gym_id} exists."},404
    
    return jsonify(gym_schema.dump(gym))


@gym_bp.route('/climbs/')
def get_gym_climbs():
    """Function to get all the climbs for all gyms"""
    gyms_with_climbs = Gym.query.options(
        joinedload(Gym.climbs)
    ).order_by(Gym.name).all()

    result = []
    for gym in gyms_with_climbs:
        gym_data = {
            "gym_id": gym.id,
            "name": gym.name,
            "city": gym.city,
            "climbs": climbs_output_schema.dump(gym.climbs)
        }
        result.append(gym_data)
    
    return jsonify(result)

@gym_bp.route('/admin/add/', methods=["POST"])
@jwt_required()
@admin_required
def add_a_gym():
    """A function to POST a gym for admins"""
    # GET JSON body data
    body_data = request.get_json()

    # Create gym from body_data using gym_schema
    new_gym = gym_schema.load(body_data, session=db.session)

    db.session.add(new_gym)
    db.session.commit()

    return jsonify(gym_schema.dump(new_gym)), 201

@gym_bp.route('/admin/remove/<int:gym_id>', methods=["DELETE"])
@jwt_required()
@admin_required
def remove_a_gym(gym_id):
    # GET statement: SELECT * FROM gyms WHERE Gym.id = gym_id;
    stmt = db.select(Gym).where(Gym.id==gym_id)
    gym = db.session.scalar(stmt)

    if not gym:
        return {"message": f"Gym with id {gym_id} does not exist."}, 404
    
    db.session.delete(gym)
    db.session.commit()

    return {"message": f"Gym with id {gym_id} deleted successfully."}, 200

@gym_bp.route('/admin/update/<int:gym_id>/', methods=["PUT", "PATCH"])
@jwt_required()
@admin_required
def update_a_gym_record(gym_id):
    """Function to UPDATE a single gym from the database for admins"""
    # GET statement: SELECT * FROM gyms WHERE Gym.id = gym_id
    stmt = db.select(Gym).where(Gym.id==gym_id)
    gym = db.session.scalar(stmt)

    # Check that the gym exists
    if not gym:
        return {"message": f"Gym with id {gym_id} does not exist."}, 404
    
    # GET JSON body data
    body_data = request.get_json()

    # Load data into gym through gym_schema
    updated_gym = gym_schema.load(
        body_data,
        instance = gym,
        session = db.session,
        partial = True
    )

    db.session.add(updated_gym)
    db.session.commit()

    return {
        "message": "Gym updated successfully.",
        "details": jsonify(gym_schema.dump(updated_gym))
    }, 200