from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from init import db
from models import Company
from schemas import company_schema, companies_schema
from utils import admin_required

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

@company_bp.route('/<int:company_id>')
def get_a_company(company_id):
    """Funtion to GET single company record from the database"""
    # GET statement: SELECT * FROM companies WHERE Company.id == company_id
    stmt = db.select(Company).where(Company.id==company_id)
    company = db.session.scalar(stmt)

    if not company:
        {"message": f"Company with id {company_id} not found."}, 404

    return jsonify(company_schema.dump(company))

@company_bp.route('/admin/add/', methods=["POST"])
@jwt_required()
@admin_required
def add_a_company():
    """Function to POST a single company to the database for admins"""
    # GET JSON body data
    body_data = request.get_json()

    # Create company using company schema
    new_company = company_schema.load(body_data, session=db.session)

    db.session.add(new_company)
    db.session.commit()

    return jsonify(company_schema.dump(new_company))

@company_bp.route('/admin/remove/<int:company_id>', methods=["DELETE"])
@jwt_required()
@admin_required
def remove_a_company(company_id):
    """Function to DELETE a company from the database for admins"""
    # GET statement: SELECT * FROM company WHERE Company.id = company_id;
    stmt = db.select(Company).where(Company.id==company_id)
    company = db.session.scalar(stmt)

    if not company:
        return {"message": f"Company with id {company_id} does not exist."}, 404
    
    db.session.delete(company)
    db.session.commit()

    return {"message": f"Company with id {company_id} deleted successfully."}, 200

@company_bp.route('/admin/update/<int:company_id>/', methods=["PUT", "PATCH"])
@jwt_required()
@admin_required
def update_a_company_record(company_id):
    """Function to UPDATE a single company from the database for admins"""
    # GET statement: SELECT * FROM companies WHERE Company.id = company_id
    stmt = db.select(Company).where(Company.id==company_id)
    company = db.session.scalar(stmt)

    # Check that the company exists
    if not company:
        return {"message": f"Company with id {company_id} does not exist."}, 404
    
    # GET JSON body data
    body_data = request.get_json()

    # Load data into company through company_schema
    updated_company = company_schema.load(
        body_data,
        instance = company,
        session = db.session,
        partial = True
    )

    db.session.add(updated_company)
    db.session.commit()

    return jsonify(company_schema.dump(updated_company))