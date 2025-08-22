from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate

from models import Climb

class ClimbInputSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Climb
        load_instance = True
        include_fk = True

    # Validation for difficulty grade: must be between 1 * 10
    difficulty_grade = fields.Integer(
        validate=[validate.Range(min=1, max=10, error="Rating must be between 1-10")]
    )

    # Validation for set_date: must be date
    set_date = fields.Date(required=False)

class ClimbOutputSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Climb
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("id", "gym_name", "username", "style_name", "difficulty_grade", "set_date")
        ordered = True
    
    gym_name = fields.String(attribute="gym.name")
    username = fields.String(attribute="user.username")
    style_name = fields.String(attribute="styles.name")

climb_input_schema = ClimbInputSchema()
climb_inputs_schema = ClimbInputSchema(many=True)
climb_output_schema = ClimbOutputSchema()
climbs_output_schema = ClimbOutputSchema(many=True)