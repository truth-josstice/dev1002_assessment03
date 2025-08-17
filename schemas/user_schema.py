from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.users import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("_password_hash",)

user_schema = UserSchema()
users_schema = UserSchema(many=True)