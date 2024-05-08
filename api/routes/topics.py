from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Query, Path, Response, status
from db import DatabaseManager, database_manager
import dependencies
import queries
from models import CreateTopic, UpdateTopic
from shared import slap
import mapping

router = APIRouter()


@router.get("/topics", tags=["Topics"])
async def get_topics(response: Response,
                     db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        topics_unmapped = db["topics"].find()
        topics_mapped = queries.get_all_topics(topics_unmapped)
        response.status_code = status.HTTP_200_OK
        return topics_mapped
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.get("/topics/{topicKey}", tags=["Topics"])
async def get_topic_from_topicKey(response: Response, topicKey: str, verification = Depends(dependencies.get_verify_signature),
                     db: DatabaseManager = Depends(database_manager.get_database)):
    try: 
        topic = queries.get_topic_from_topicKey(db["topics"].find(), topicKey)
        if topic is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "Topic not found"}
        response.status_code = status.HTTP_200_OK
        return topic
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/topic", tags=["Topics"])
async def create_topic(response: Response, new_topic: CreateTopic, db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        topic_db, topic = mapping.create_topic(new_topic)
        if topic:
            db["topics"].insert_one(topic_db)
            response.status_code = status.HTTP_201_CREATED
            return vars(topic)
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put("/topic/{topicKey}", tags=["Topics"])
async def update_topic(response: Response, topicKey: str, updated_topic: UpdateTopic,
                           db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        topic = queries.get_topic_from_topicKey(db["topics"].find(), topicKey)
        if topic:
            filter_item = {"_id": topic["topicKey"]}
            updated_data = {
                "$set": {
                    "name": updated_topic.name,
                    "description": updated_topic.description
                }
            }
            db["topics"].update_one(filter_item, updated_data)
            response.status_code = status.HTTP_202_ACCEPTED
            return {"message": "Item successfully updated"}
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete("/topic/{topicKey}", tags=["Topics"])
async def delete_topic(response: Response, topicKey: str,
                           db: DatabaseManager = Depends(database_manager.get_database)):
    try:
        topic = queries.get_topic_from_topicKey(db["topics"].find(), topicKey)
        if topic:
            db["topics"].delete_one(topic)
            response.status_code = status.HTTP_202_ACCEPTED
            return {"message": "Item successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")
    except Exception as e:
        raise HTTPException(500, str(e))
