from app.models.base_entity import BaseModel
from app.models.amenity import Amenity
from app.models.review import Review
from app.models.user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.reviews = []
        self.amenities = []

    def validate_title(self, title):
        pass
    def validate_price(self, price):
        pass

    def validate_latitude(self, latitude):
        pass

    def validate_longitude(self, longitude):
        pass

    def validate_owner(self, owner: "User"):
        pass

    def add_review(self, review: "Review"):
        pass

    def add_amenity(self, amenity):
        pass
    def validate_description(self, description):

        pass