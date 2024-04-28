from typing import Annotated
from db import get_database
from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_user_collection(token: str):
    db = get_database()
    try:
        yield db["users"]
    finally:
        db.close()