from app.models.base_entity import BaseModel
class User(BaseModel):
    def __init__(self,first_name:str, last_name:str, email:str,is_admin:bool=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
    def register(self):
        # Logic to register the user
        pass
    def update_profile(self):
        # Logic to update user profile
        pass
    def delete(self):
        # Logic to delete the user
        pass
    def add_place(self, place):
        """Add a place to the user's list of places."""
        self.places.append(place)

