from init import db

class Gym(db.Model):
    __tablename__ = "gyms"

    id = db.Column(db.Integer, primary_key=True)
    # company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    city = db.Column(db.String, nullable=True)
    street_address = db.Column(db.String, nullable=True, unique=True)
    name = db.Column(db.String, nullable=False)

    # company = db.relationship("Company", back_populates="gyms")