from app.models.base_entity import BaseModel
from app import db, bcrypt
from sqlalchemy.orm import relationship
# Amenity model for the HBnB application.

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    places = db.relationship('Place', secondary='place_amenity', backref='amenities', lazy=True)
    # Constructor for the Amenity class
    #relationships are defined to link amenities with places
    def __init__(self, name, description=""):
        super().__init__()
        if len(name) > 50:
            raise ValueError("Amenity name must be 50 characters or fewer")
        self.name = name
        self.description = description