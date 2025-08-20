from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from models.gym_ratings import GymRating

class GymRatingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GymRating
        load_instance = True
        include_fk = False
        include_relationships = True
        fields = ("gym", "user", "recommended_skill_level", "difficulty_rating", "review")
        ordered = True
    
    recommended_skill_level = Nested("SkillLevelSchema", only=("id", "level"))
    gym = Nested("GymSchema", only=("id", "name"))
    user = Nested("UserSchema", only=("id", "username", "user_skill_level.level"))


gym_rating_schema = GymRatingSchema()
gym_ratings_schema = GymRatingSchema(many=True)