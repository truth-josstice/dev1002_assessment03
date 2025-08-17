from init import db

class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    website = db.Column(db.String, unique=True)
    
    # one to many with gyms
    gym = db.relationship("Gym", back_populates="company", cascade="all, delete")