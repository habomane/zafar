from models import CreateUser, User
from shared import slap

def create_user(create_user: CreateUser): 
    uuid = slap.generate_UUID()
    user = User(uuid, create_user.publicKey)
    return {"_id": uuid, **vars(user)}, user

def set_user(user):
    user = { "uuid": user["uuid"]}
    return user

