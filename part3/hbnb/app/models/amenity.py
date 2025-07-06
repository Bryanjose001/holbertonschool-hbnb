from app.models.base_entity import BaseModel
from app import db, bcrypt
# Amenity model for the HBnB application.
class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    # Constructor for the Amenity class
    
    def __init__(self, name, description=""):
        super().__init__()
        if len(name) > 50:
            raise ValueError("Amenity name must be 50 characters or fewer")
        self.name = name
        self.description = description