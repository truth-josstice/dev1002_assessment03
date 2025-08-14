from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.users import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True