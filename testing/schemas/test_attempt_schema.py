from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import RelatedList, Nested
from marshmallow import fields

from models.attempts import Attempt
from schemas.climb_schema import ClimbSchema

class AttemptSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Attempt
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("id", "climb", "username", "fun_rating", 
                "comments", "completed", "attempt_date")
        ordered = True
        
    climb = Nested("ClimbSchema", only=("id", "gym_name"))
    username = fields.String(attribute="user.username")

attempt_schema = AttemptSchema()
attempts_schema = AttemptSchema(many=True)