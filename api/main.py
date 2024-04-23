from fastapi import FastAPI
from models import User, CreateUser
import db
import mapping

app = FastAPI()
db = db.get_database()

## defining collections
users = db["users"]
profiles = db["profiles"]
posts = db["posts"]
comments = db["comments"]

## users 
@app.post("/register")
async def register_user(create_user: CreateUser):
    user_db, user = mapping.create_user(create_user)
    users.insert_one(user_db)
    profile_db, profile = mapping.create_generic_profile(user)
    profiles.insert_one(profile_db)
    return vars(profile)
    


## posts 


## comments 



