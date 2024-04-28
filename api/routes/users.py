from fastapi import APIRouter, HTTPException, Response, status, Depends, Query, Header, Path
from db import DatabaseManager, database_manager
import dependencies
from typing import Annotated
import queries

router = APIRouter()


@router.get("/user/", tags=["Users"], 
            name="Retrieve user uuid from public key", 
            description="Providing the public key will allow users to retrieve the corresponding uuid. This unique identifier value can be used to further identify user profiles.")
async def get_user_from_publicKey(response: Response, verification = Depends(dependencies.get_verify_signature),
                                  db : DatabaseManager = Depends(database_manager.get_database)):
    try:
        all_users = db["users"].find()
        user = queries.get_user_from_publicKey(all_users, verification["publicKey"])
        response.status_code = status.HTTP_200_OK
        return user
    except Exception as e:
        raise HTTPException(500, detail=str(e))