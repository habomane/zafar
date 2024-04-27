from fastapi import FastAPI, HTTPException
from models import User, CreateUser, GetProfile
import db
import queries
import mapping
from shared import slap


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

## should recieve a signature in the parameters? 
@app.get("/profile/username/{username}")
async def get_profile_from_username(username, signature: str, date: str, publicKey: str):
    try: 
        if not slap.verify_signature(signature, date, publicKey):
            raise HTTPException(status_code=403, detail="Message could not be verified.")
        response = queries.get_profile_from_username(profiles.find(), username)
        return response
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")


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



