from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import RelatedList, Nested
from marshmallow import fields

from models.gym import Gym
from schemas.climb import ClimbSchema

class GymSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Gym
        load_instance = True
        include_fk = True
        include_relationships = True
        fields=("id", "company_name", "name", "city", "street_address", "climbs")
        ordered = True

    company_name = fields.String(attribute="company.name")
    climbs = RelatedList(Nested("ClimbSchema", exclude=("id",)))

gym_schema = GymSchema()
gyms_schema = GymSchema(many=True)