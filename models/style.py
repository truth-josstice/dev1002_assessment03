from init import db

class Style(db.Model):
    """Represents a list of all styles available for the user to choose from."""
    __tablename__ = "styles"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False, unique=True)
    description: str = db.Column(db.String, nullable=False, unique=True)

    climbs = db.relationship("Climb", back_populates="styles")