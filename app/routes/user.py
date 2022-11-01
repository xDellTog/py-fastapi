from fastapi import APIRouter
from app.schemas.user import User

from app.services.user import UserService

userRouter = APIRouter(
    prefix="/users",
    tags=["user"]
)

@userRouter.get("/")
def read():
    service = UserService()
    return service.findAll()

@userRouter.get("/{id}")
def read(id: int):
    service = UserService()
    return service.findOne(id)

@userRouter.post("/")
def create(user: User):
    service = UserService()
    return service.create(user)

@userRouter.put("/{id}")
def update(id: int, user: User):
    service = UserService()
    return service.update(id, user)

@userRouter.delete("/{id}")
def delete(id: int):
    service = UserService()
    return service.delete(id)
