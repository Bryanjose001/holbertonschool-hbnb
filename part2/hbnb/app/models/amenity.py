from app.models.base_entity import BaseModel
class Amenity(BaseModel):
    def __init__(self, name:str):
        super().__init__()
        self.name = name
    def create(self):
        # Logic to create an amenity
        pass
    def update(self):
        # Logic to update amenity details
        pass
    def delete(self):
        # Logic to delete the amenity
        pass
    def list(self):
        # Logic to list all amenities
        pass