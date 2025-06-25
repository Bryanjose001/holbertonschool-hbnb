from app.models.base_entity import BaseModel

class User(BaseModel):
 def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        super().__init__()
        self.first_name = self.validate_name(first_name, "First name")
        self.last_name = self.validate_name(last_name, "Last name")
        self.email = self.validate_email(email)
        self.is_admin = is_admin

def validate_name(self, name: str, field: str):
        if not name or not isinstance(name, str):
            raise ValueError(f"{field} must be a non-empty string")
        return name.strip()

def validate_email(self, email: str):
    if not email or not isinstance(email, str) or "@" not in email:
        raise ValueError("A valid email address is required")
        return email.strip().lower()

def register(self):
    print(f"Registering user: {self.email}")
    pass

def update_profile(self):
    print(f"Updating profile for user: {self.email}")
    pass

def delete(self):
    print(f"Deleting user: {self.email}")
    pass

#def add_place(self, place):
    #if not isinstance(place, Place):
       #raise ValueError("Only Place instances can be added")
    #self.places.append(place)