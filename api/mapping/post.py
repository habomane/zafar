from models import CreatePost, Post
from shared import slap
from . import set_comment

def create_post(create_post: CreatePost): 
    postKey = slap.generateUUID()
    post = Post(postKey, create_post.title, create_post.description, create_post.date,
                create_post.ownerUuid, create_post.topicKey)
    return {"_id": postKey, **vars(post)}, post

def set_post(post):
    comments = []
    if post["comments"] != []:
        for comment in post.comment:
            mapped_comment = set_comment(comment) 
            comments.append(mapped_comment)
        
    post = {
        "postKey": post["postKey"],
        "title": post["title"],
        "description": post["description"],
        "ownerUuid": post["ownerUuid"],
        "date": post["date"],
        "topicKey": post["topicKey"],
        "comments": comments
    }
    
    return post

