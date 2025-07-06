from app.models.place import Place
from app import db
from app.persistence.repository import SQLAlchemyRepository

class PlaceRepository(SQLAlchemyRepository):
    """Repository for managing Place entities."""
    
    def __init__(self):
        super().__init__(Place)

    def get_places_by_user(self, user_id):
        """Get all places owned by a specific user."""
        return self.model.query.filter_by(user_id=user_id).all()

    def get_places_by_city(self, city_id):
        """Get all places located in a specific city."""
        return self.model.query.filter_by(city_id=city_id).all()