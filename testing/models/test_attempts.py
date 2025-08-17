from init import db

from datetime import date
from sqlalchemy import text

class Attempt(db.Model):
    """Represents a user attempt at a climb with ratings and completion status."""
    __tablename__ = "attempts"

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"))
    climb_id: int = db.Column(db.Integer, db.ForeignKey("climbs.id"))
    fun_rating: int = db.Column(db.Integer, nullable=False)
    comments: str | None = db.Column(db.String)
    completed: bool = db.Column(db.Boolean, default=False)
    attempt_date: date = db.Column(db.Date, server_default=text("CURRENT_DATE"))

    climb = db.relationship("Climb", back_populates="attempt")
    user = db.relationship("User", back_populates="attempt")