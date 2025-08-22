from init import db

class SkillLevel(db.Model):
    """Represents a list of all skill levels available to the user."""
    __tablename__ = "skill_levels"

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(32), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)

    user = db.relationship("User", back_populates="user_skill_level")
    gym_rating = db.relationship("GymRating", back_populates="recommended_skill_level")