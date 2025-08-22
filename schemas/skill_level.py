from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import SkillLevel

class SkillLevelSchema(SQLAlchemyAutoSchema):
    """Represents the different skill levels available to be chosen by the user"""
    class Meta:
        model = SkillLevel
        load_instance = True

skill_level_schema = SkillLevelSchema()
skill_levels_schema = SkillLevelSchema(many=True)