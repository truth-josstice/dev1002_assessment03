from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.gym_ratings import GymRating

class GymRatingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GymRating
        load_instance = True
        include_fk = True

gym_rating_schema = GymRatingSchema()
gym_ratings_schema = GymRatingSchema(many=True)