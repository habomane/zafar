from pydantic import BaseModel

class User(BaseModel):
    uuid: str
    public_key: str
    
class Profile(BaseModel):
    username: str
    description: str | None = None
    uuid: str

class UpdateProfile(BaseModel):
    username: str
    description: str | None = None


    