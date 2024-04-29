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
