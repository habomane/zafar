from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries
from models import CreateComment, UpdateComment
from shared import slap
import mapping

router = APIRouter()

@router.get("/comments/{postKey}", tags=["Comments"])
async def get_comments_from_postKey(response: Response, postKey: str, db: DatabaseManager = Depends(database_manager.get_database)):
    try: 
        post = queries.get_comments_from_postKey(db["comments"].find(), postKey)
        if post is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "Comments not found"}
        response.status_code = status.HTTP_200_OK
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/comment/{commentKey}", tags=["Comments"])
async def get_comment_from_commentKey(response: Response, commentKey: str, db: DatabaseManager = Depends(database_manager.get_database)):
    try: 
        post = queries.get_comment_from_commentKey(db["posts"].find(), commentKey)
        if post is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "Comment not found"}
        response.status_code = status.HTTP_200_OK
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/comment", tags=["Comments"])
async def post_comment(response: Response, new_comment: CreateComment, db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        comment_db, comment = mapping.create_comment(new_comment)
        if comment:
            db["comments"].insert_one(comment_db)
            response.status_code = status.HTTP_201_CREATED
            return vars(comment)
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put("/comment/{commentKey}", tags=["Comments"])
async def update_comment(response: Response, commentKey: str, updated_comment: UpdateComment,
                           db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        comment = queries.get_comment_from_commentKey(db["comments"].find(), commentKey)
        if comment:
            filter_item = {"_id": comment["commentKey"]}
            updated_data = {
                "$set": {
                    "name": updated_comment.name,
                    "description": updated_comment.description
                }
            }
            db["comments"].update_one(filter_item, updated_data)
            response.status_code = status.HTTP_202_ACCEPTED
            return {"message": "Item successfully updated"}
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete("/comment/{commentKey}", tags=["Comments"])
async def delete_comment(response: Response, commentKey: str,
                           db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        comment = queries.get_comment_from_commentKey(db["comments"].find(), commentKey)
        if comment:
            db["comments"].delete_one(comment)
            response.status_code = status.HTTP_202_ACCEPTED
            return {"message": "Item successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))