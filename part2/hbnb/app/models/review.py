from app.models.base_entity import BaseModel
class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = self.validate_comment(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)

    def validate_comment(self, text):
        if not text or not isinstance(text, str):
            raise ValueError("Review text must be a non-empty string")
        return text.strip()

    def validate_rating(self, rating):
        if not isinstance(rating, (int, float)) or not (1 <= rating <= 5):
            raise ValueError("Rating must be a number between 1 and 5")
        return float(rating)

    def validate_place(self, place: ["Place"]):
        if not place or not isinstance(place, Place):
            raise ValueError("Place must be a valid Place instance")
        return place

    def validate_user(self, user: ["User"]):
        if not user or not isinstance(user, User):
            raise ValueError("User must be a valid User instance")
        return user
