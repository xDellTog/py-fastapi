import os
from fastapi import FastAPI
from app.routes.user import user_router
from app.routes.auth import auth_router

app = FastAPI(
    title=os.environ.get("APP_TITLE"), 
    description=os.environ.get("APP_DESCRIPTION"), 
    version=os.environ.get("APP_VERSION")
)

app.include_router(user_router)
app.include_router(auth_router)
