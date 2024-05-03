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

@router.get("/comments/{postKey}")