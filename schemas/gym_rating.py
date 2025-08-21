from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from models import GymRating

class GymRatingOutputSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GymRating
        load_instance = True
        include_fk = False
        include_relationships = True
        fields = ("gym", "user", "recommended_skill_level", "difficulty_rating", "review")
        ordered = True
    
    recommended_skill_level = Nested("SkillLevelSchema", only=("level",))
    gym = Nested("GymSchema", only=("id", "name"))
    user = Nested("UserSchema", only=("id", "username", "user_skill_level.level"))

gym_rating_output_schema = GymRatingOutputSchema()
gym_ratings_output_schema = GymRatingOutputSchema(many=True)

class GymRatingInputSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GymRating
        load_instance = True
        include_fk = True

gym_rating_input_schema = GymRatingInputSchema()