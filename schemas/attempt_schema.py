from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.attempts import Attempt

class AttemptSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Attempt
        load_instance = True
        include_fk = True

attempt_schema = AttemptSchema()
attempts_schema = AttemptSchema(many=True)