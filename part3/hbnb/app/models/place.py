from app.models.base_entity import BaseModel
from app.models.user import User
from app.models.review import Review
from app.extensions import db
from sqlalchemy.orm import relationship
# Place model for the HBnB application.

place_amenity = db.Table("place_amenity",
    db.Column("place_id", db.String(36), db.ForeignKey("places.id"), primary_key=True),
    db.Column("amenity_id", db.String(36), db.ForeignKey("amenities.id"), primary_key=True)
)



class Place(BaseModel):
    __tablename__ = 'places'
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True) 
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner = db.Column(db.String(36), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='user_places', lazy=True)
    reviews = relationship('Review', backref='reviews_place', lazy=True)
    amenities = relationship('Amenity', secondary=place_amenity, backref='amenities_places', lazy=True)
    

    def __init__(self, title, description, price, latitude, longitude, owner,user_id):
        super().__init__()


        # Use setters to apply validation
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.user_id = user_id

        self.reviews = []
        self.amenities = []

    # --- Review & Amenity Helpers (unchanged) ---
    def add_review(self, review: "Review"):
        if not isinstance(review, Review):
            raise ValueError("Only Review instances can be added")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
