from flask import Blueprint, jsonify, request

from init import db
from models.gyms import Gym
from schemas.gym_schema import gym_schema, gyms_schema

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