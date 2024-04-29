from models import User, Profile
from shared import generate_username

def create_generic_profile(user: User):
    random_username = generate_username()
    profile = Profile(user.uuid, random_username)
    return {"_id": user.uuid, **vars(profile)}, profile

def set_profile(profile):
    profile = Profile(profile["uuid"], profile["username"], profile["description"])
    return profile


