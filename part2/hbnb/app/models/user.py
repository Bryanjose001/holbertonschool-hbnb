from base_entity import BaseEntity
class User(BaseEntity):
    def __init__(self,first_name:str, last_name:str, email:str, password:str,is_admin:bool=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
    def register(self):
        # Logic to register the user
        pass
    def update_profile(self):
        # Logic to update user profile
        pass
    def delete(self):
        # Logic to delete the user
        pass

