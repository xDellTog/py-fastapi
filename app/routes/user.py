from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserUpdate
from app.services.user import UserService
from app.services.auth import AuthService

auth_service = AuthService()
user_service = UserService()

user_router = APIRouter(
    prefix="/users",
    tags=["user"],
    dependencies=[Depends(auth_service.authentication_token)]
)

@user_router.get("/")
def read():
    return user_service.findAll()

@user_router.get("/{id}")
def read(id: int):
    return user_service.findOne(id)

@user_router.post("/")
def create(user: UserCreate):
    return user_service.create(user)

@user_router.put("/{id}")
def update(id: int, user: UserUpdate):
    return user_service.update(id, user)

@user_router.delete("/{id}")
def delete(id: int):
    return user_service.delete(id)
