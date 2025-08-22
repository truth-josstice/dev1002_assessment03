from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from marshmallow import fields, validate

from models import Attempt

class AttemptOutputSchema(SQLAlchemyAutoSchema):
    """Display schema for users, does not include all data from the climbs"""
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
    """Display schema for admins with all climb details included"""
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
    """Input schema with validation for all attempt POST routes"""
    class Meta:
        model = Attempt
        load_instance = True
        include_fk = True

    # Validation for fun_rating: must be between 1 & 5
    fun_rating = fields.Integer(
        required=True,
        validate=[
            validate.Range(min=1, max=5, error="Ratings must be between 1-5")
        ]
    )

    # Validation for comments: must be below 500 chars
    comments = fields.String(
        validate=[validate.Length(max=500, error="Comments cannot exceed 500 characters")]
    )

    # Validation for completed: defaults to false
    completed = fields.Boolean(load_default=False)


attempt_output_schema = AttemptOutputSchema()
attempts_output_schema = AttemptOutputSchema(many=True)
admin_attempts_schema = AdminAttemptSchema(many=True)
attempt_input_schema = AttemptInputSchema()
attempts_input_schema = AttemptInputSchema(many=True)