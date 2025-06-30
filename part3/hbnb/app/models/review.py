from app.models.base_entity import BaseModel

class Review(BaseModel):
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
