from pydantic import BaseModel

class User():
    def __init__(self, uuid, public_key):
        self.uuid = uuid
        self.public_key = public_key

class CreateUser(BaseModel):
    public_key: str
    
class Profile():
    def __init__(self, username, uuid, description = None):
        self.uuid = uuid
        self.username = username, 
        self.description = description

class UpdateProfile(BaseModel):
    username: str
    description: str | None = None


    