from app.models.base_entity import BaseModel
from app.extensions import db
import uuid
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

class Review(BaseModel):
    """Review model for the HBnB application."""
    __tablename__ = 'reviews'
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )

    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place = db.Column(db.String(36), nullable=False)
    user = db.Column(db.String(36), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    place = relationship('Place', backref='place_reviews', lazy=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='user_reviews', lazy=True)


    
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text       # Validation happens here
        self.rating = rating
        self.place = place
        self.user = user
