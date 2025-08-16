from datetime import date

from init import db

class Climb(db.Model):
    """Represents a climb posted by a user, with a style, difficulty and the date it was set if known"""
    __tablename__ = "climbs"

    id: int = db.Column(db.Integer, primary_key=True)
    gym_id: int = db.Column(db.Integer, db.ForeignKey("gyms.id"))
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"))
    style: str = db.Column(db.String, nullable=False)
    difficulty_grade: str = db.Column(db.String, nullable=False)
    set_date: date = db.Column(db.Date)

    gym = db.relationship("Gym", back_populates="climbs") # Type: Relationship
    user = db.relationship("User", back_populates="climbs", cascade="all, delete") # Type: Relationship