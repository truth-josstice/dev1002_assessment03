from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from utils import admin_required

from init import db

from models import SkillLevel, Style
from schemas import (
    skill_level_schema,
    skill_levels_schema, 
    style_schema,
    styles_schema)

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

@info_bp.route('/admin/add-style/', methods = ["POST"])
@jwt_required()
@admin_required
def add_style():
    # GET JSON body data
    body_data = request.get_json()

    # Create style record using style_schema
    new_style = style_schema.load(body_data, session=db.session)

    db.session.add(new_style)
    db.session.commit()

    return {"message": f"Style {new_style.name} added successfully"}, 201


@info_bp.route('/admin/add-skill/', methods = ["POST"])
@jwt_required()
@admin_required
def add_skill():
    # GET JSON body data
    body_data = request.get_json()

    # Create style record using style_schema
    new_skill = skill_level_schema.load(body_data, session=db.session)

    db.session.add(new_skill)
    db.session.commit()

    return {"message": f"Style {new_skill.level} added successfully"}, 201

