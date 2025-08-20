from flask import Blueprint, jsonify, request

from init import db
from models import Climb
from schemas import climb_schema, climbs_schema

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
    
    return jsonify(climbs_schema.dump(climbs))