from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import RelatedList, Nested
from marshmallow import fields

from models import Attempt

class AttemptOutputSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Attempt
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("id", "climb", "fun_rating", 
                "comments", "completed", "attempted_at")
        ordered = True
        
    climb = Nested("ClimbOutputSchema", only=("id", "gym_name", "style_name"))


class AdminAttemptSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Attempt
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("id", "climb", "fun_rating", 
                "comments", "completed", "attempted_at")
        ordered = True

    climb = Nested("ClimbOutputSchema")


class AttemptInputSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Attempt
        load_instance = True
        include_fk = True


attempt_output_schema = AttemptOutputSchema()
attempts_output_schema = AttemptOutputSchema(many=True)
admin_attempts_schema = AdminAttemptSchema(many=True)
attempt_input_schema = AttemptInputSchema()
attempts_input_schema = AttemptInputSchema(many=True)