from init import db

class GymRating(db.Model):
    __tablename__ = "gym_ratings"

    gym_id = db.Column(db.Integer, db.ForeignKey("gyms.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    difficulty_rating = db.Column(db.Integer, nullable=False)
    recommended_skill_level = db.Column(db.String, nullable=False)
    review = db.Column(db.String)

    gym = db.relationship("Gym", back_populates="gym_rating")
    user = db.relationship("User", back_populates="gym_rating")