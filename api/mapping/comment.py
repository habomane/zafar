from models import CreateComment, Comment
from shared import slap

def create_comment(create_comment: CreateComment): 
    uuid = slap.generateUUID()
    comment = Comment(**create_comment)
    return {"_id": uuid, **vars(comment)}, comment

def set_post(comment):
    comment = {
        "comment_key": comment["comment_key"],
        "comment": comment["comment"],
        "owner_uuid": comment["owner_uuid"],
        "date": comment["date"],
        "post_key": comment["post_key"]
    }
    
    return comment

