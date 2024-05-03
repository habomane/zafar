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

@router.get("/topics/{topicKey}", tags=["Topics"])
async def get_topic_from_topicKey(response: Response, verification = Depends(dependencies.get_verify_signature),
                     db: DatabaseManager = Depends(database_manager.get_database)):
    return {"topics"}

@router.post("/topic", tags=["Topics"])
async def create_topic():
    return {""}

@router.put("/topic/{topicKey}", tags=["Topics"])
async def update_topic():
    return {""}

@router.delete("/topic/{topicKey}", tags=["Topics"])
async def delete_topic():
    return {""}
