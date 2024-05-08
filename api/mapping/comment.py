from models import CreateComment, Comment
from shared import slap

def create_comment(create_comment: CreateComment, postKey): 
    commentKey = slap.generateUUID()
    comment = Comment(create_comment.comment, commentKey, postKey,
                      create_comment.date, create_comment.ownerUuid)
    return {"_id": commentKey, **vars(comment)}, comment

def set_comment(comment):
    comment = {
        "commentKey": comment["commentKey"],
        "comment": comment["comment"],
        "ownerUuid": comment["ownerUuid"],
        "date": comment["date"],
        "postKey": comment["postKey"]
    }
    
    return comment


