from models import CreateTopic, Topic
from shared import slap

def create_topic(create_topic: CreateTopic): 
    topicKey = slap.generateUUID()
    topic = Topic(topicKey, create_topic.name,
                  create_topic.description, create_topic.ownerUuid)
    return {"_id": topicKey, **vars(topic)}, topic

def set_topic(topic):
    topic = {
        "topicKey": topic["topicKey"],
        "name": topic["name"],
        "description": topic["description"],
        "ownerUuid": topic["ownerUuid"]
    }
    
    return topic

