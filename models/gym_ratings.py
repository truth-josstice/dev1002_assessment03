from init import db

class GymRating(db.Model):
    __tablename__ = "gym_ratings"

    id = db.Column(db.Integer, primary_key=True)
    gym_id = db.Column(db.Integer, db.ForeignKey("gyms.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    difficulty_rating = db.Column(db.Integer, nullable=False)
    recommended_skill_level = db.Column(db.String, nullable=False)
    review = db.Column(db.String)