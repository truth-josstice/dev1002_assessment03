from flask import Blueprint, jsonify, request
from sqlalchemy import func, select

from collections import Counter

from init import db
from models.gym_ratings import GymRating
from models.gyms import Gym
from models.skill_level import SkillLevel
from schemas.gym_rating_summary_schema import gym_rating_summaries_schema
from schemas.skill_level_schema import skill_level_schema
from schemas.gym_rating_schema import gym_rating_schema, gym_ratings_schema

gym_rating_bp = Blueprint("gym_rating", __name__, url_prefix="/gym_ratings")


@gym_rating_bp.route('/')
def get_gym_info():
    """
    Complex query function to get information from gym_ratings by gym and display the aggregate results.
    """
    # Select: id, avg difficulty rating, review count (each row is unique reviews)
    stmt = (
        select(
            GymRating.gym_id,
            func.avg(GymRating.difficulty_rating).label("average_rating"),
            func.count().label("review_count"),
        )
        .group_by(GymRating.gym_id) # Group by Gym
        .order_by(GymRating.gym_id) # Order by Gym Id
    )

    results = db.session.execute(stmt).all() # Executes the SQL Query

    # Check that reviews exist
    if not results:
        return {"message": "No gyms have been reviewed yet!"},404
    
    # Get all gyms with their relationships loaded, filter for unique entries (joins may cause duplicate data)
    gyms = db.session.scalars(
        select(Gym).options(
            db.joinedload(Gym.company),
            db.joinedload(Gym.climbs),
            db.joinedload(Gym.gym_rating)
        )
    ).unique().all()
    
    gym_dict = {gym.id: gym for gym in gyms}

     # Get all ratings with skill level relationships loaded
    all_ratings = db.session.scalars(
        select(GymRating).options(db.joinedload(GymRating.recommended_skill_level))
    ).all()

    # Group by gym and find most common skill level
    gym_skill_levels = {}
    for rating in all_ratings:
        gym_id = rating.gym_id
        if gym_id not in gym_skill_levels:
            gym_skill_levels[gym_id] = []
        
        serialized_skill = skill_level_schema.dump(rating.recommended_skill_level)
        gym_skill_levels[gym_id].append(serialized_skill)

    # Build customised response data
    response_data = []
    for result in results:
        gym_id = result.gym_id
        gym = gym_dict.get(gym_id)
        
        if not gym:
            continue  # Skip if gym not found (shouldn't happen)
        
        skill_levels = gym_skill_levels.get(gym_id, [])
        
        # Find most common skill level
        if skill_levels:
            level_counts = Counter(sl['id'] for sl in skill_levels)
            most_common_id = level_counts.most_common(1)[0][0]
            recommended_skill = next(sl for sl in skill_levels if sl['id'] == most_common_id)
        else:
            recommended_skill = None
        
        response_data.append({
            "gym": gym,  # Pass the full gym object - schema will handle serialization
            "average_difficulty_rating": float(result.average_rating),
            "total_reviews": result.review_count,
            "recommended_skill_level": recommended_skill
        })
    
    # Serialize and return using schema
    return jsonify(gym_rating_summaries_schema.dump(response_data))

@gym_rating_bp.route('/details/')
def get_gym_ratings():
    '''Function to GET all individual gym_ratings from the database'''
    # GET statement: SELECT * FROM gym_ratings; --> shows all details of every review
    stmt = db.select(GymRating)
    gym_ratings = db.session.scalars(stmt).all()

    if not gym_ratings:
        return {"message": "No gym_rating records found."}, 404
    
    return jsonify(gym_ratings_schema.dump(gym_ratings))