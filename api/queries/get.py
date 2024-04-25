import mapping

def get_all_profiles(profiles):
    all_profiles = []
    for profile in profiles:
        profile_mapped = mapping.set_profile(profile)
        all_profiles.append(profile_mapped)
    return all_profiles

def get_profile_from_username(profiles, username):
    for profile in profiles:
        if profile["username"] == username:
            return mapping.set_profile(profile)

def get_profile_from_uuid(profiles, uuid):
    for profile in profiles:
        if profile["uuid"] == uuid:
            return mapping.set_profile(profile)

def get_user_from_uuid(users, uuid):
    for user in users:
        if user["uuid"] == uuid:
            return user

def get_user_from_public_key(users, public_key):
    for user in users:
        if user["publicKey"] == public_key:
            return user