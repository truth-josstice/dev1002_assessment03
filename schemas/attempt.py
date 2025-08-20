from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import RelatedList, Nested
from marshmallow import fields

from models import Attempt

class AttemptSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Attempt
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("id", "climb", "fun_rating", 
                "comments", "completed", "attempted_at")
        ordered = True
        
    climb = Nested("ClimbOutputSchema", only=("id", "gym_name", "style_name"))

attempt_schema = AttemptSchema()
attempts_schema = AttemptSchema(many=True)