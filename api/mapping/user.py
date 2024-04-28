from models import CreateUser, User, Profile
from shared import slap, generate_username


def create_user(create_user: CreateUser): 
    uuid = slap.generate_UUID()
    user = User(uuid, create_user.publicKey)
    return {"_id": uuid, **vars(user)}, user

def create_generic_profile(user: User):
    random_username = generate_username()
    profile = Profile(user.uuid, random_username)
    return {"_id": user.uuid, **vars(profile)}, profile

def set_profile(profile):
    profile = Profile(profile["uuid"], profile["username"], profile["description"])
    return profile

def set_user(user):
    user = { "uuid": user["uuid"]}
    return user

