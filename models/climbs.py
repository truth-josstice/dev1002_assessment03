from sqlalchemy import text
from init import db

class Climb(db.Model):
    __tablename__ = "climbs"

    id = db.Column(db.Integer, primary_key=True)
    gym_id = db.Column(db.Integer, db.ForeignKey("gyms.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    style = db.Column(db.String, nullable=False)
    difficulty_grade = db.Column(db.String, nullable=False)
    set_date = db.Column(db.Date)