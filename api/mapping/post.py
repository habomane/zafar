from models import CreatePost, Post
from shared import slap

def create_post(create_post: CreatePost): 
    uuid = slap.generateUUID()
    post = Post(**create_post)
    return {"_id": uuid, **vars(post)}, post

def set_post(post):
    post = {
        "post_key": post["post_key"],
        "title": post["title"],
        "description": post["description"],
        "owner_uuid": post["owner_uuid"],
        "date": post["date"],
        "topic_key": post["topic_key"]
    }
    
    return post

