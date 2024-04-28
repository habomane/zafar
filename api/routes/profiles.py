from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
from shared import slap
import queries

router = APIRouter()

@router.get("/profiles", tags=["Profiles"])
async def get_all_profiles(response: Response, date: Annotated[str, Query()],
                           signature: Annotated[str, Header()], publicKey: Annotated[str, Header()],
                           db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        if not slap.verify_signature(signature, date, publicKey):
            raise HTTPException(status_code=403, detail="Signature could not be verified.")
        profiles = queries.get_all_profiles(db["profiles"].find())
        response.status_code = status.HTTP_200_OK
        return profiles
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": "Something went wrong. Please try again later"}

@router.get("/profiles/username/{username}", tags=["Profiles"])
async def get_profile_from_username(response: Response, username: Annotated[str, Path()], date: Annotated[str, Query()], signature: Annotated[str, Header()], 
                                    publicKey: Annotated[str, Header()], db: DatabaseManager = Depends(database_manager.get_database)
                                    ):
    try: 
        if not slap.verify_signature(signature, date, publicKey):
            raise HTTPException(status_code=403, detail="Signature could not be verified.")
        profile = queries.get_profile_from_username(db["profiles"].find(), username)
        response.status_code = status.HTTP_200_OK
        return profile
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": "Something went wrong. Please try again later"}
    
@router.get("/profiles/username/{uuid}", tags=["Profiles"])
async def get_profile_from_uuid(response: Response, uuid: Annotated[str, Path()], date: Annotated[str, Query()], signature: Annotated[str, Header()], 
                                    publicKey: Annotated[str, Header()], db: DatabaseManager = Depends(database_manager.get_database)
                                    ):
    try: 
        if not slap.verify_signature(signature, date, publicKey):
            raise HTTPException(status_code=403, detail="Signature could not be verified.")
        profile = queries.get_profile_from_uuid(db["profiles"].find(), uuid)
        response.status_code = status.HTTP_200_OK
        return profile
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": "Something went wrong. Please try again later"}