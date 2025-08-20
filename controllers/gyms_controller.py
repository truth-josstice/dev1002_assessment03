from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload

from init import db
from models.gym import Gym

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
    
    return jsonify(gyms_schema.dump(gyms))

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
