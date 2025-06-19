from base_entity import BaseEntity
class Place(BaseEntity):
    def __init__(self, title:str, description:str,price:str, latitude:float,longitude:float,owner:):
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
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