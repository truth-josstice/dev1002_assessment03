from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.climbs import Climb

class ClimbSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Climb
        load_instance = True
        include_fk = True

climb_schema = ClimbSchema()
climbs_schema = ClimbSchema(many=True)