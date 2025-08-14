from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.gyms import Gym

class GymSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Gym
        load_instance = True
        include_fk = True

gym_schema = GymSchema()
gyms_schema = GymSchema(many=True)