from app.models.base_entity import BaseModel
from app.models.amenity import Amenity
from app.models.review import Review
from app.models.user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = self.validate_description(description)
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.reviews = []
        self.amenities = []

    def validate_title(self, title):
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        return title.strip()

    def validate_description(self, description):
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        return description.strip()

    def validate_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        return float(price)

    def validate_latitude(self, latitude):
        if not isinstance(latitude, (int, float)) or not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be a number between -90 and 90")
        return float(latitude)

    def validate_longitude(self, longitude):
        if not isinstance(longitude, (int, float)) or not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be a number between -180 and 180")
        return float(longitude)

    def validate_owner(self, owner: "User"):
        if not owner or not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance")
        return owner

    def add_review(self, review: "Review"):
        if not isinstance(review, Review):
            raise ValueError("Only Review instances can be added")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)