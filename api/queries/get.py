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

def get_user_from_publicKey(users, publicKey):
    for user in users:
        if user["publicKey"] == publicKey:
            return mapping.set_user(user)