from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries
from models import CreatePost, UpdatePost
from shared import slap
import mapping

router = APIRouter()

@router.get("/posts", tags=["Posts"])
async def get_posts(response: Response, db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        posts_unmapped = db["posts"].find()
        posts_mapped = queries.get_all_posts(posts_unmapped)
        response.status_code = status.HTTP_200_OK
        return posts_mapped
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.get("/post/{postKey}", tags=["Posts"])
async def get_post_from_postKey(response: Response, postKey: str, db: DatabaseManager = Depends(database_manager.get_database)):
    try: 
        post = queries.get_post_from_postKey(db["posts"].find(), postKey)
        if post is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "Post not found"}
        response.status_code = status.HTTP_200_OK
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/posts/topic/{topicKey}", tags=["Posts"])
async def get_posts_from_topicKey(response: Response, topicKey: str, db: DatabaseManager = Depends(database_manager.get_database)):
    try: 
        post = queries.get_posts_from_topicKey(db["posts"].find(), topicKey)
        if post == []:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "No posts were found for this topic"}
        response.status_code = status.HTTP_200_OK
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/posts/username/{username}", tags=["Posts"],
            name="Get Posts For User Through Username")
async def get_posts_from_username(response: Response, username: str, db: DatabaseManager = Depends(database_manager.get_database)):
    try: 
        ## Find uuid from user
        profile = queries.get_profile_from_username(db["profiles"].find(), username)
        if profile is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "Username not found"}
        ## Find posts with the corresponding uuid
        post = queries.get_posts_from_uuid(db["posts"].find(), profile.uuid)
        if post == []:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "No posts were found for this user"}
        response.status_code = status.HTTP_200_OK
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/posts/uuid/{uuid}", tags=["Posts"],
            name="Get Posts For User Through UUID")
async def get_posts_uuid(response: Response, uuid: str, db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        ## Find posts with the corresponding uuid
        post = queries.get_posts_from_uuid(db["posts"].find(), uuid)
        if post == []:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "No posts were found for this user"}
        response.status_code = status.HTTP_200_OK
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/post", tags=["Posts"])
async def create_post(response: Response, new_post: CreatePost, db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        post_db, post = mapping.create_post(new_post)
        if post:
            db["posts"].insert_one(post_db)
            response.status_code = status.HTTP_201_CREATED
            return vars(post)
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put("/post/{postKey}", tags=["Posts"])
async def update_post(response: Response, updated_post: UpdatePost, postKey: str, db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        post = queries.get_post_from_postKey(db["posts"].find(), postKey)
        if post:
            filter_item = {"_id": post["postKey"]}
            updated_data = {
                "$set": {
                    "title": updated_post.title,
                    "description": updated_post.description
                }
            }
            db["posts"].update_one(filter_item, updated_data)
            response.status_code = status.HTTP_202_ACCEPTED
            return {"message": "Item successfully updated"}
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete("/post/{postKey}", tags=["Posts"])
async def delete_post(response: Response, postKey: str, db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        post = queries.get_post_from_postKey(db["posts"].find(), postKey)
        if post:
            db["posts"].delete_one(post)
            response.status_code = status.HTTP_202_ACCEPTED
            return {"message": "Item successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

        