from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import RelatedList, Nested
from marshmallow import fields, validate

from models import Company
# from schemas.gym_schema import GymSchema

class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        load_instance = True
        include_relationships=True
        ordered=True
        fields=("id", "name", "website", "gyms")
    
    gyms=RelatedList(Nested("GymSchema", only=("name", "street_address")))

    # Validation for website: must be website

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)