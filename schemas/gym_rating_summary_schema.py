from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from marshmallow import fields
from models.gym_ratings import GymRating

class GymRatingSummarySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GymRating
        load_instance = False
        fields = ("gym", "average_difficulty_rating", "total_reviews", "recommended_skill_level")
        ordered = True
    
    # Gym details from GymSchema
    gym = Nested("GymSchema", only=("name", "city"))
    
    # Aggregate fields
    average_difficulty_rating = fields.Float(required=True)
    total_reviews = fields.Int(required=True)
    recommended_skill_level = Nested("SkillLevelSchema", only=("level", "description"))

gym_rating_summary_schema = GymRatingSummarySchema()
gym_rating_summaries_schema = GymRatingSummarySchema(many=True)