from pydantic import BaseModel

class Topic(BaseModel):
    topic_key: str
    name: str
    description: str | None = None
    uuid: str

class UpdateTopic(BaseModel):
    name: str
    description: str | None = None


    