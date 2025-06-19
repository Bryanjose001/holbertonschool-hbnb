from base_entity import BaseEntity
class Review(BaseEntity):
    def __init__(self, text, place, rating,user):
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
