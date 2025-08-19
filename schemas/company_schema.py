from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import RelatedList, Nested

from models.company import Company
# from schemas.gym_schema import GymSchema

class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        load_instance = True
        include_relationships=True
        ordered=True
        fields=("id", "name", "website", "gyms")
    
    gyms=RelatedList(Nested("GymSchema", only=("name", "street_address")))

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)