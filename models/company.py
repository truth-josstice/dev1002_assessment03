from init import db

class Company(db.Model):
    __tablename__ = "companies"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False, unique=True)
    website: str = db.Column(db.String(255), nullable=False, unique=True)
    
    # one to many with gyms
    gym = db.relationship("Gym", back_populates="company", cascade="all, delete-orphan")