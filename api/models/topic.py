from pydantic import BaseModel

class CreateTopic(BaseModel):
    topic_key: str
    name: str
    description: str | None = None
    owner_uuid: str

class Topic:
    def __init__(self, topic_key, name, description, owner_uuid):
        self.topic_key = topic_key
        self.name = name
        self.description = description
        self.owner_uuid = owner_uuid

class UpdateTopic(BaseModel):
    name: str
    description: str | None = None


    