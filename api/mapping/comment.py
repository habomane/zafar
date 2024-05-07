from models import CreateComment, Comment
from shared import slap

def create_comment(create_comment: CreateComment): 
    uuid = slap.generateUUID()
    comment = Comment(**create_comment)
    return {"_id": uuid, **vars(comment)}, comment

def set_comment(comment):
    comment = {
        "commentKey": comment["commentKey"],
        "comment": comment["comment"],
        "ownerUuid": comment["ownerUuid"],
        "date": comment["date"],
        "postKey": comment["postKey"]
    }
    
    return comment


