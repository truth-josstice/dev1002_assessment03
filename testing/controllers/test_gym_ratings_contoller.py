from flask import Blueprint, jsonify, request

from init import db
from models.gym_ratings import GymRating
from schemas.gym_rating_schema import gym_rating_schema, gym_ratings_schema

gym_rating_bp = Blueprint("gym_rating", __name__, url_prefix="/gym_ratings")

@gym_rating_bp.route('/')
def get_gym_ratings():
    '''Function to GET multiple gym_ratings from the database'''
    # GET statement: SELECT * FROM gym_ratings;
    stmt = db.select(GymRating)
    gym_ratings = db.session.scalars(stmt).all()

    if not gym_ratings:
        return {"message": "No gym_rating records found."}, 404
    
    return jsonify(gym_ratings_schema.dump(gym_ratings))