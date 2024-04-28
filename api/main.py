from typing import Annotated
from fastapi import FastAPI, HTTPException, Header,  Path, Query, status, Request, Depends
from models import User, CreateUser, GetProfile
from db import DatabaseManager, database_manager
import queries
import mapping
import routes.profiles
from shared import slap
import routes


app = FastAPI()
app.include_router(routes.users.router)
app.include_router(routes.profiles.router)
## defining collections
    
@app.get("/itefdkms/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(alas="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
    k: Annotated[str | None, Header(alias="item-header")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if k:
        results.update({"header": k})
    return results

## users 



# @app.get("/profile/uuid/{uuid}")
# async def get_profile_from_uuid(uuid):
#     all_profiles = profiles.find()
#     response = queries.get_profile_from_uuid(all_profiles, uuid)
#     return response

# @app.get("/user/{publicKey}")
# async def get_user_from_publicKey(publicKey):
#     all_users = users.find()
#     response = queries.get_user_from_publicKey(all_users, publicKey)
#     return response

# @app.post("/register")
# async def register_user(create_user: CreateUser):
#     user_db, user = mapping.create_user(create_user)
#     users.insert_one(user_db)
#     profile_db, profile = mapping.create_generic_profile(user)
#     profiles.insert_one(profile_db)
#     return vars(profile)


## posts 


## comments 



