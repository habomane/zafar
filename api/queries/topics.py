import mapping

def get_all_topics(topics):
    all_topics = []
    for topic in topics:
        topic_mapped = mapping.set_topic(topic)
        all_topics.append(topic_mapped)
    return all_topics


def get_topic_from_topicKey(topics, topicKey):
    for topic in topics:
        if topic["topicKey"] == topicKey:
            return mapping.set_topic(topic)
