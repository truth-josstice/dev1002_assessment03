from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import RelatedList, Nested
from marshmallow import fields

from models.gym_ratings import GymRating

class GymRatingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GymRating
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("gym_id", "user_id", "gym_name", "username", "difficulty_rating",
                  "recommended_skill_level", "review")
        ordered = True
    
    gym_name = fields.String(attribute="gym.name")
    username = fields.String(attribute="use.username")

gym_rating_schema = GymRatingSchema()
gym_ratings_schema = GymRatingSchema(many=True)