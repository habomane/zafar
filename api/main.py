from fastapi import FastAPI
import routes

app = FastAPI()
app.include_router(routes.users.router)
app.include_router(routes.profiles.router)
