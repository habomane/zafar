import mapping

def get_all_comments(comments):
    all_comments = []
    for comment in comments:
        comment_mapped = mapping.set_comment(comment)
        all_comments.append(comment_mapped)
    return all_comments


def get_comments_from_postKey(comments, commentKey):
    all_comments = []
    for comment in comments:
        if comment["commentKey"] == commentKey:
            all_comments.append(mapping.set_comment(comment))
    return all_comments
        
        
def get_comment_from_commentKey(comments, commentKey):
    for comment in comments:
        if comment["commentKey"] == commentKey:
            return mapping.set_comment(comment)
