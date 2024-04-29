from pydantic import BaseModel

class CreateComment(BaseModel):
    comment: str
    comment_key: str
    post_key: str
    date: str
    owner_uuid: str

class Comment:
    def __init__(self, comment, comment_key, post_key, date, owner_uuid):
        self.comment = comment
        self.comment_key = comment_key
        self.post_key = post_key
        self.date = date
        self.owner_uuid: owner_uuid
        
class UpdateComment(BaseModel):
    comment: str
    post_key: str
