from pydantic import BaseModel

class CreatePost(BaseModel):
    title: str
    description: str | None = None
    date: str
    owner_uuid: str
    topic_key: str
    post_key: str

class Post:
    def __init__(self, title, description, date, owner_uuid, topic_key, post_key):
        self.title = title
        self.description = description
        self.date = date
        self.owner_uuid = owner_uuid
        self.topic_key = topic_key
        self.post_key = post_key

class UpdatePost(BaseModel):
    title: str
    description: str | None = None


    
    