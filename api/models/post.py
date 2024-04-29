from pydantic import BaseModel

class Post(BaseModel):
    title: str
    description: str | None = None
    date: str
    owner_uuid: str
    topic_key: str
    post_key: str

class UpdatePost(BaseModel):
    title: str
    description: str | None = None


    
    