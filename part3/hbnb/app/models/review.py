from app.models.base_entity import BaseModel
from app import db, bcrypt
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
    rating = db.Column(db.Float, nullable=False)
    place = db.Column(db.String(36), nullable=False)
    user = db.Column(db.String(36), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    place = relationship('Place', backref='reviews', lazy=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='reviews', lazy=True)
    
    def __init__(self, text, rating, place, user):
        super().__init__()
        self._text = None
        self._rating = None
        self._place = None
        self._user = None

        self.text = text       # Validation happens here
        self.rating = rating
        self.place = place
        self.user = user

    # --- Text (Comment) ---
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Review text must be a non-empty string")
        self._text = value.strip()

    # --- Rating ---
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (value, (int, float)) or not (1 <= value <= 5):
            raise ValueError("Rating must be a number between 1 and 5")
        self._rating = float(value)
