from app.models.base_entity import BaseModel
class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = self.validate_comment(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)

    def validate_comment(self, text):

        pass
    def validate_rating(self, rating):

        pass
    def validate_place(self, place:"Place"):
        
        pass

    def validate_user(self, user:"User"):

       pass