from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.skill_level import SkillLevel

class SkillLevelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SkillLevel
        load_instance = True

skill_level_schema = SkillLevelSchema()
skill_levels_schema = SkillLevelSchema(many=True)