from fastapi import FastAPI
from pydantic import BaseModel

class Name(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "hello world"}


@app.post('/name/')
async def remind_name(name : Name):
    return name