from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries
from models import CreateUser, UpdateProfile
from shared import slap
import mapping

router = APIRouter()

@router.get("/posts", tags=["Posts"])
async def get_posts(response: Response):
    return {"posts"}

@router.get("/posts/{topicKey}", tags=["Posts"])
async def get_posts_for_topic(topicKey):
    return {""}

@router.get("/posts/{username}", tags=["Posts"],
            name="Get Posts For User Through Username")
async def get_posts_username(username):
    return {""}

@router.get("/posts/{uuid}", tags=["Posts"],
            name="Get Posts For User Through UUID")
async def get_posts_uuid(uuid):
    return {""}

@router.post("/post", tags=["Posts"])
async def create_post(new_post):
    return {""}

@router.put("/post/{postKey}", tags=["Posts"])
async def update_post():
    return {""}

@router.delete("/post/{postKey}", tags=["Posts"])
async def delete_post():
    return {""}

        