from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries

router = APIRouter()

@router.get("/profiles", tags=["Profiles"])
async def get_all_profiles(response: Response, verification = Depends(dependencies.get_verify_signature),
                           db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        profiles = queries.get_all_profiles(db["profiles"].find())
        response.status_code = status.HTTP_200_OK
        return profiles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/profiles/username/{username}", tags=["Profiles"])
async def get_profile_from_username(response: Response, username: Annotated[str, Path()],
                                    verification = Depends(dependencies.get_verify_signature), db: DatabaseManager = Depends(database_manager.get_database)
                                    ):
    try: 
        profile = queries.get_profile_from_username(db["profiles"].find(), username)
        response.status_code = status.HTTP_200_OK
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/profiles/username/{uuid}", tags=["Profiles"])
async def get_profile_from_uuid(response: Response, uuid: Annotated[str, Path()], 
                                verification = Depends(dependencies.get_verify_signature),  db: DatabaseManager = Depends(database_manager.get_database)
                                    ):
    try: 
        profile = queries.get_profile_from_uuid(db["profiles"].find(), uuid)
        response.status_code = status.HTTP_200_OK
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))