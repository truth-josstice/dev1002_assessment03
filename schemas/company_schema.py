from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.company import Company

class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        load_instance = True

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)