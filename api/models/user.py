from pydantic import BaseModel


class CreateUser(BaseModel):
    public_key: str

class GetProfile(BaseModel):
    username: str
class User():
    def __init__(self, uuid: str, public_key: str):
        self.uuid = uuid
        self.public_key = public_key
    
class Profile():
    def __init__(self, uuid: str, username: str, description=None):
        self.uuid = uuid
        self.username = username
        self.description = description

class UpdateProfile(BaseModel):
    username: str
    description: str | None = None


    