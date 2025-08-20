from flask import Blueprint, jsonify, request

from init import db
from models.company import Company
from schemas.company_schema import company_schema, companies_schema

company_bp = Blueprint("company", __name__, url_prefix="/companies")



@company_bp.route('/')
def get_companies():
    '''Function to GET multiple companies from the database'''
    # GET statement: SELECT * FROM companies;
    stmt = db.select(Company)
    companies = db.session.scalars(stmt).all()

    if not companies:
        return {"message": "No company records found."}, 404
    
    return jsonify(companies_schema.dump(companies))