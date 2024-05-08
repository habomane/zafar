from pydantic import BaseModel

class CreateComment(BaseModel):
    comment: str
    date: str
    ownerUuid: str

class Comment:
    def __init__(self, comment, commentKey, postKey, date, ownerUuid):
        self.comment = comment
        self.commentKey = commentKey
        self.postKey = postKey
        self.date = date
        self.ownerUuid = ownerUuid
        
class UpdateComment(BaseModel):
    comment: str
    postKey: str
