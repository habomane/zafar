from models import CreatePost, Post
from shared import slap
from . import set_comment

def create_post(create_post: CreatePost): 
    postKey = slap.generateUUID()
    post = Post(postKey, create_post.title, create_post.description, create_post.date,
                create_post.owner_uuid, create_post.topic_key)
    return {"_id": postKey, **vars(post)}, post

def set_post(post):
    comments = []
    
    for comment in post.comment:
        mapped_comment = set_comment(comment) 
        comments.append(mapped_comment)
        
    post = {
        "post_key": post["post_key"],
        "title": post["title"],
        "description": post["description"],
        "owner_uuid": post["owner_uuid"],
        "date": post["date"],
        "topic_key": post["topic_key"],
        "comments": comments
    }
    
    return post

