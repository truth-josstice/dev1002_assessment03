from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested, RelatedList

from models import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        # exclude = ("_password_hash",)
        ordered = True
        fields = ("id", "username", "email", "first_name", "last_name", "user_skill_level")
    
    user_skill_level = Nested("SkillLevelSchema")


user_schema = UserSchema()
users_schema = UserSchema(many=True)