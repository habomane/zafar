from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries

router = APIRouter()

@router.get("/profiles", tags=["Profiles"],
            name="Retrieve a list of all existing profiles.")
async def get_all_profiles(response: Response, verification = Depends(dependencies.get_verify_signature),
                           db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        profiles = queries.get_all_profiles(db["profiles"].find())
        response.status_code = status.HTTP_200_OK
        return profiles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/profiles/username/{username}", tags=["Profiles"],
            name="Retrieve a profile by providing the username",
            description="Providing the username as a parameter will allow users to retrieve the corresponding profile information. A signature and public key must be included in the header to verify the request date.")
async def get_profile_from_username(response: Response, username: Annotated[str, Path()],
                                    verification = Depends(dependencies.get_verify_signature), db: DatabaseManager = Depends(database_manager.get_database)
                                    ):
    try: 
        profile = queries.get_profile_from_username(db["profiles"].find(), username)
        response.status_code = status.HTTP_200_OK
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/profiles/username/{uuid}", tags=["Profiles"],
            name="Retrieve a profile by providing the unique user identifier",
            description="Providing the uuid as a parameter will allow users to retrieve the corresponding profile information. A signature and public key must be included in the header to verify the request date.")
async def get_profile_from_uuid(response: Response, uuid: Annotated[str, Path()], 
                                verification = Depends(dependencies.get_verify_signature),  db: DatabaseManager = Depends(database_manager.get_database)
                                    ):
    try: 
        profile = queries.get_profile_from_uuid(db["profiles"].find(), uuid)
        response.status_code = status.HTTP_200_OK
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))