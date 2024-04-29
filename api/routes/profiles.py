from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries
from models import CreateUser
from shared import slap
import mapping

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

@router.post("/profile/register", tags=["Profiles"],
            name="Register a new profile")
async def register_profile(new_user: CreateUser, response: Response, 
                           verification = Depends(dependencies.post_verify_signature),
                           db: DatabaseManager = Depends(database_manager.get_databasebas)):
    try:
        if not slap.verifySignature(verification["signature"], user, verification["publicKey"]):
            raise HTTPException(403, detail="Signature could not be verified.")
        user_db, user = mapping.create_user(new_user)
        if user:
            db["users"].insert_one(user_db)
            profile_db, profile = mapping.create_generic_profile(user)
            db["profiles"].insert_one(profile_db)
            return vars(profile)
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put("/profile/update/{uuid}", tags=["Profiles"],
            name="Update a profile")
async def update_profile():
    try:
        pass
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

