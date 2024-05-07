import mapping

def get_all_posts(posts):
    all_posts = []
    for post in posts:
        post_mapped = mapping.set_post(post)
        all_posts.append(post_mapped)
    return all_posts

def get_post_from_postKey(posts, postKey):
    for post in posts:
        if post["postKey"] == postKey:
            return mapping.set_post(post)

def get_posts_from_uuid(posts, uuid):
    user_posts = []
    for post in posts:
        if post["ownerUuid"] == uuid:
            user_posts.append(mapping.set_post(post))
    return user_posts


def get_posts_from_topicKey(posts, topicKey):
    topic_posts = []
    for post in posts:
        if post["topicKey"] == topicKey:
            topic_posts.append(mapping.set_post(post))
    return topic_posts


def get_full_profile_from_uuid(profiles, uuid):
    for profile in profiles:
        if profile["uuid"] == uuid:
            return profile
    
