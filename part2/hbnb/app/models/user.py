from app.models.base_entity import BaseModel


class User(BaseModel):
 def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        super().__init__()
        if not first_name or not last_name:
            raise ValueError("must be a non-empty string")
        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError("must be 50 char or fewer")
        if not email or "@" not in email:
            raise ValueError("A valid email address is required")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

def register(self):
    #print(f"Registering user: {self.email}")
    pass

def update_profile(self):
    #print(f"Updating profile for user: {self.email}")
    pass

def delete(self):
    #print(f"Deleting user: {self.email}")
    pass

#def add_place(self, place):
    #if not isinstance(place, Place):
       #raise ValueError("Only Place instances can be added")
    #self.places.append(place)