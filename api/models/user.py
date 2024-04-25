from pydantic import BaseModel


class CreateUser(BaseModel):
    publicKey: str

class GetProfile(BaseModel):
    username: str
class User():
    def __init__(self, uuid: str, publicKey: str):
        self.uuid = uuid
        self.publicKey = publicKey
    
class Profile():
    def __init__(self, uuid: str, username: str, description=None):
        self.uuid = uuid
        self.username = username
        self.description = description

class UpdateProfile(BaseModel):
    username: str
    description: str | None = None


    