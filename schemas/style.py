from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.style import Style

class StyleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Style
        load_instance = True

style_schema = StyleSchema()
styles_schema = StyleSchema(many=True)