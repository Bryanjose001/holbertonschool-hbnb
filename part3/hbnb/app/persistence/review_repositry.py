from app.models.review import Review
from app import db
from app.persistence.repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):
    """Repository for managing Review entities."""
    
    def __init__(self):
        super().__init__(Review)

    def get_reviews_by_place(self, place_id):
        """Get all reviews for a specific place."""
        return self.model.query.filter_by(place=place_id).all()

    def get_reviews_by_user(self, user_id):
        """Get all reviews made by a specific user."""
        return self.model.query.filter_by(user=user_id).all()
    