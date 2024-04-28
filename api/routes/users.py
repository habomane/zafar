from fastapi import APIRouter
import db
import queries

router = APIRouter()

@router.get("/users/", tags=["User"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["Users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["Users"])
async def read_user(username: str):
    return {"username": username}

@router.get("/user/{publicKey}", tags=["User"])
async def get_user_from_publicKey(publicKey):
    all_users = users.find()
    response = queries.get_user_from_publicKey(all_users, publicKey)
    return response