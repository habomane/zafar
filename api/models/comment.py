from pydantic import BaseModel

class Comment(BaseModel):
    comment: str
    comment_key: str
    post_key: str
    date: str
    owner_uuid: str
    
class UpdateComment(BaseModel):
    comment: str
    post_key: str
