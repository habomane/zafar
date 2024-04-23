from pydantic import BaseModel

class Name(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None