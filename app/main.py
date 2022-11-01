import os
from fastapi import FastAPI
from app.routes.user import userRouter

app = FastAPI(
    title=os.environ.get("APP_TITLE"), 
    description=os.environ.get("APP_DESCRIPTION"), 
    version=os.environ.get("APP_VERSION")
)

app.include_router(userRouter)
