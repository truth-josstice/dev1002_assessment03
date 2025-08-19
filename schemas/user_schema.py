from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from models.users import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        exclude = ("_password_hash",)
    
    skill_level = Nested("SkillLevelSchema")


user_schema = UserSchema()
users_schema = UserSchema(many=True)