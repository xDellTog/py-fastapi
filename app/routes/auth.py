from fastapi import APIRouter
from app.schemas.user import  UserAuth
from app.services.auth import AuthService

auth_router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
)

authService = AuthService()

@auth_router.post("/login")
def create(user: UserAuth):
    return authService.generate_access_token(user)