from pydantic import BaseModel

class CreatePost(BaseModel):
    title: str
    description: str | None = None
    date: str
    ownerUuid: str
    topicKey: str

class Post:
    def __init__(self,  postKey, title, description, date, ownerUuid, topicKey):
        self.title = title
        self.description = description
        self.date = date
        self.ownerUuid = ownerUuid
        self.topicKey = topicKey
        self.postKey = postKey
        self.comments = []
    
    def update_comments(self, comments):
        self.comments = comments

class UpdatePost(BaseModel):
    title: str
    description: str | None = None


    
    