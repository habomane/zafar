from fastapi import FastAPI
import routes
import routes.comments
import routes.posts
import routes.topics

app = FastAPI()
app.include_router(routes.users.router)
app.include_router(routes.profiles.router)
app.include_router(routes.topics.router)
app.include_router(routes.posts.router)
app.include_router(routes.comments.router)
