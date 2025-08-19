from init import db

class SkillLevel(db.Model):
    """Represents a list of all skill levels available to the user."""
    __tablename__ = "skill_levels"

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)

    user = db.relationship("User", back_populates="skill_level")
    gym_rating = db.relationship("GymRating", back_populates="skill_level")