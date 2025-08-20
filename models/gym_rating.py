from init import db

class GymRating(db.Model):
    __tablename__ = "gym_ratings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    gym_id = db.Column(db.Integer, db.ForeignKey("gyms.id"), nullable=False)
    difficulty_rating = db.Column(db.Integer, nullable=False)
    skill_level_id = db.Column(db.Integer, db.ForeignKey("skill_levels.id"), nullable=False)
    review = db.Column(db.String)

    # Add unique user + review constraints
    __table_args__ = (db.UniqueConstraint('user_id', 'gym_id', name='_user_gym_uc'),)

    gym = db.relationship("Gym", back_populates="gym_rating")
    user = db.relationship("User", back_populates="gym_rating")
    recommended_skill_level = db.relationship("SkillLevel", back_populates="gym_rating")