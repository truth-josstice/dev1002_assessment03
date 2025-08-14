from sqlalchemy import text
from init import db

class Climb(db.Model):
    __tablename__ = "climbs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    style = db.Column(db.String, nullable=False)
    difficulty_grade = db.Column(db.String, nullable=False)
    set_date = db.Column(db.Date, server_default=text("CURRENT_DATE"))