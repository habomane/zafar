from fastapi import FastAPI
from models import User, CreateUser, GetProfile
import db
import queries
import mapping

app = FastAPI()
db = db.get_database()

## defining collections
users = db["users"]
profiles = db["profiles"]
posts = db["posts"]
comments = db["comments"]

## users 
@app.get("/profiles")
async def get_all_profile():
    all_profiles = profiles.find()
    response = queries.get_all_profiles(all_profiles)
    return response


@app.get("/profile/username/{username}")
async def get_profile_from_username(username):
    all_profiles = profiles.find()
    response = queries.get_profile_from_username(all_profiles, username)
    return response

@app.get("/profile/uuid/{uuid}")
async def get_profile_from_uuid(uuid):
    all_profiles = profiles.find()
    response = queries.get_profile_from_uuid(all_profiles, uuid)
    return response

@app.get("/user/{publicKey}")
async def get_user_from_publicKey(publicKey):
    all_users = users.find()
    response = queries.get_user_from_publicKey(all_users, publicKey)
    return response

@app.post("/register")
async def register_user(create_user: CreateUser):
    user_db, user = mapping.create_user(create_user)
    users.insert_one(user_db)
    profile_db, profile = mapping.create_generic_profile(user)
    profiles.insert_one(profile_db)
    return vars(profile)


## posts 


## comments 



