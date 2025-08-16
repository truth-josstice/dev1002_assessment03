from init import db

class Gym(db.Model):
    __tablename__ = "gyms"

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    city = db.Column(db.String, nullable=False)
    street_address = db.Column(db.String, unique=True)
    name = db.Column(db.String, nullable=False)

    company = db.relationship("Company", back_populates="gyms")
    climbs = db.relationship("Climb", back_populates="gyms")