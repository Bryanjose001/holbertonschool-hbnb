from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository

class AmenityRepository(SQLAlchemyRepository):
    """Repository for managing Amenity entities."""
    
    def __init__(self):
        super().__init__(Amenity)

    def get_amenities_by_place(self, place_id):
        """Get all amenities associated with a specific place."""
        return self.model.query.filter_by(place_id=place_id).all()

    def get_amenities_by_user(self, user_id):
        """Get all amenities created by a specific user."""
        return self.model.query.filter_by(user_id=user_id).all()