from part2.hbnb.app.models.base_entity import BaseModel
from part2.hbnb.app.models.user import User
from part2.hbnb.app.models.place import Place


class Review(BaseModel):
    def __init__(self, text:str, place:Place, rating:int,user:User):
        self.rating = rating
        self.text = text
        self.place = place 
        self.user = user
    def create(self):
        # Logic to create a review
        pass
    def update(self):
        # Logic to update review details
        pass
    def delete(self):
        # Logic to delete the review
        pass
    def list(self):
        # Logic to list all reviews
        pass
