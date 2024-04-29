from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries
from models import CreateTopic
from shared import slap
import mapping

router = APIRouter()


@router.get("/topics", tags=["Topics"])
async def get_topics(response: Response, verification = Depends(dependencies.get_verify_signature),
                     db: DatabaseManager = Depends(database_manager.get_database)):
    return {"topics"}

