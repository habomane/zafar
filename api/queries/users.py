import mapping

def get_user_from_publicKey(users, publicKey):
    for user in users:
        if user["publicKey"] == publicKey:
            return mapping.set_user(user)
        
def get_full_user_from_uuid(users, uuid):
    for user in users:
        if user["uuid"] == uuid:
            return user
