from fastapi import APIRouter, Depends, Query, Header, Path
from db import DatabaseManager, database_manager
from shared import slap
from typing import Annotated
import queries

router = APIRouter()


@router.get("/user/", tags=["Users"], 
            name="Retrieve user uuid from public key", 
            description="Providing the public key will allow users to retrieve the corresponding uuid. This unique identifier value can be used to further identify user profiles.")
async def get_user_from_publicKey(publicKey : Annotated[str, Header()], date : Annotated[str, Query()], signature: Annotated[str, Header()], 
                                  db : DatabaseManager = Depends(database_manager.get_database)):
    all_users = db["users"].find()
    response = queries.get_user_from_publicKey(all_users, publicKey)
    return response