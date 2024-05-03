from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries
from models import CreateUser, UpdateProfile
from shared import slap
import mapping

router = APIRouter()

@router.get("/comments", tags=["Comments"])
async def get_comments(response: Response):
    return {"comments"}

@router.get("/comments/{postKey}", tags=["Comments"])
async def get_comments_from_postKey():
    return {""}

@router.get("/comments/{commentKey}", tags=["Comments"])
async def get_comments_from_commentKey():
    return {""}

@router.post("/comment", tags=["Comments"])
async def post_comment():
    return {""}

@router.put("/comment/{commentKey}", tags=["Comments"])
async def update_comment():
    return {""}

@router.delete("/comment/{commentKey}", tags=["Comments"])
async def delete_comment():
    return {""}