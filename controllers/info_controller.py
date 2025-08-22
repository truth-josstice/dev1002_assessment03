from flask import Blueprint, jsonify

from init import db

from models import SkillLevel, Style
from schemas import skill_levels_schema, styles_schema

info_bp = Blueprint('info', __name__, url_prefix="/learn")

@info_bp.route('/styles/')
def get_styles():
    """Retrieves all style records from the styles table and displays to visitor"""
    # GET statement: SELECT * FROM skill_levels;
    stmt = db.select(Style)
    styles = db.session.scalars(stmt)

    # Check that styles exist
    if not styles:
        return {"message": "No styles found"}, 404
    
    return jsonify(styles_schema.dump(styles))

@info_bp.route('/skill-levels/')
def get_skill_levels():
    """Retreives all skill level records from the skill_levels table and displays to visitor"""
    # Get statement: SELECT * FROM skill_levels;
    stmt = db.select(SkillLevel)
    skills = db.session.scalars(stmt)

    # Check skills exist
    if not skills:
        return {"message": "No skills found"}, 404
    
    return jsonify(skill_levels_schema.dump(skills))