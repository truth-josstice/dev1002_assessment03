from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload
from sqlalchemy import func, select

from init import db
from models.gyms import Gym
from models.gym_ratings import GymRating

from schemas.climb_schema import climbs_schema
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

@gym_bp.route('/info/')
def get_gym_info():
    """
    """
    stmt = (
        select(
            GymRating.gym_id,
            func.avg(GymRating.difficulty_rating).label("average__difficulty_rating"),
            func.count().label("review_count"),
            func.max(GymRating.skill_level_id).label("recommended_skill_level")
        )
        .group_by(GymRating.gym_id)
        .order_by(GymRating.gym_id)
    )

    results = db.session.execute(stmt).all()
    
    


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
            "climbs": climbs_schema.dump(gym.climbs)
        }
        result.append(gym_data)
    
    return jsonify(result)
