from init import db

from sqlalchemy import text

class Attempt(db.Model):
    __tablename__ = "attempts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    climb_id = db.Column(db.Integer, db.ForeignKey("climbs.id"))
    fun_rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False)
    attempt_date = db.Column(db.Date, server_default=text("CURRENT_DATE"))