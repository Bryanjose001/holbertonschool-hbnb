from datetime import datetime 

class BaseEntity:
    def __init__(self, id:str, created_at:datetime, updated_at:datetime):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
