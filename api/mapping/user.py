from models import CreateUser, User, Profile
from sessionless import SessionlessSecp256k1
import shared 

def get_keys():
    pass 

sl = SessionlessSecp256k1(get_keys)

def create_user(create_user: CreateUser): 
    uuid = sl.generate_UUID()
    user = User(uuid, create_user.publicKey)
    return {"_id": uuid, **vars(user)}, user

def create_generic_profile(user: User):
    random_username = shared.generate_username()
    profile = Profile(user.uuid, random_username)
    return {"_id": user.uuid, **vars(profile)}, profile

def set_profile(profile):
    profile = Profile(profile["uuid"], profile["username"], profile["description"])
    return profile

def set_user(user):
    user = { "uuid": user["uuid"]}
    return user

