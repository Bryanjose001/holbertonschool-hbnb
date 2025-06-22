from part2.hbnb.app.models.base_entity import BaseModel
from part2.hbnb.app.models.user import User

class Place(BaseModel):
    def __init__(self, title:str, description:str,price:str, latitude:float,longitude:float,owner:User):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
    def create(self):
        # Logic to create a place
        pass
    def update(self):
        # Logic to update place details
        pass
    def delete(self):
        # Logic to delete the place
        pass
    def list(self):
        # Logic to list all places
        pass
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
