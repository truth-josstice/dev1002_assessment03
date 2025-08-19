from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from models.climbs import Climb

class ClimbSchema(SQLAlchemyAutoSchema):
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


climb_schema = ClimbSchema()
climbs_schema = ClimbSchema(many=True)