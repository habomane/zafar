from pydantic import BaseModel

class CreateTopic(BaseModel):
    name: str
    description: str | None = None
    ownerUuid: str

class Topic:
    def __init__(self, topicKey, name, description, ownerUuid):
        self.topicKey = topicKey
        self.name = name
        self.description = description
        self.ownerUuid = ownerUuid

class UpdateTopic(BaseModel):
    name: str
    description: str | None = None


    