from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import RelatedList, Nested

from models import Gym

class GymSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Gym
        load_instance = True
        include_fk = False
        include_relationships = True
        fields=("id", "company", "name", "city", "street_address")
        ordered = True

    company = Nested("CompanySchema")

gym_schema = GymSchema()
gyms_schema = GymSchema(many=True)