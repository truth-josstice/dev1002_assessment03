from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested, RelatedList
from marshmallow import fields, validate

from models import User
from utils import validate_password_for_schema

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        # exclude = ("_password_hash",)
        ordered = True
        fields = ("id", "username", "email", "first_name", "last_name", "user_skill_level")
    
    user_skill_level = Nested("SkillLevelSchema")

class UserInputSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        fields = ("id", "username", "email", "password", "first_name", "last_name", "skill_level_id")

    password = fields.String(
        load_only=True, 
        required=True, 
        validate=validate_password_for_schema
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_input_schema = UserInputSchema()