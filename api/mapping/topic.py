from models import CreateTopic, Topic
from shared import slap

def create_topic(create_topic: CreateTopic): 
    uuid = slap.generateUUID()
    topic = Topic(**create_topic)
    return {"_id": uuid, **vars(topic)}, topic

def set_topic(topic):
    topic = {
        "topic_key": topic["topic_key"],
        "name": topic["name"],
        "description": topic["description"],
        "owner_uuid": topic["owner_uuid"]
    }
    
    return topic

