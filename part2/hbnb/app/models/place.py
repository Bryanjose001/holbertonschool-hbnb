from app.models.base_entity import BaseModel
from app.models.user import User
from app.models.review import Review

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self._title = None
        self._description = None
        self._price = None
        self._latitude = None
        self._longitude = None
        self._owner = None

        # Use setters to apply validation
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

        self.reviews = []
        self.amenities = []

    # --- Title ---
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Title must be a non-empty string")
        self._title = value.strip()

    # --- Description ---
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        self._description = value.strip()

    # --- Price ---
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number")
        self._price = float(value)

    # --- Latitude ---
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)) or not (-90 <= value <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = float(value)

    # --- Longitude ---
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)) or not (-180 <= value <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = float(value)

    # --- Owner ---
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not value or not isinstance(value, User):
            raise ValueError("Owner must be a valid User instance")
        self._owner = value

    # --- Review & Amenity Helpers (unchanged) ---
    def add_review(self, review: "Review"):
        if not isinstance(review, Review):
            raise ValueError("Only Review instances can be added")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
