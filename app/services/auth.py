import os
from datetime import *
from jwt import encode, decode
from app.schemas.user import User, UserAuth, UserPayload
from fastapi import Request, HTTPException
from app.services.user import UserService
from app.services.password import PasswordService

class AuthService:
    def authentication_token(self, req: Request):
        try:
            token = str(req.headers.get("authorization")).split(' ').pop()

            payload = decode(token, str(os.environ.get("JWT_SECRET")), algorithms=["HS256"])

            req.state.user = UserPayload(
                name=payload.get("name"),
                username=payload.get("username"),
            )

            return req.state.user
        except Exception as e:
            raise HTTPException(status_code=401, detail="User unauthorized") from e
    
    def generate_access_token(self, user_auth: UserAuth):
        user_service = UserService()
        user: User = user_service.login(user_auth.username)
        
        if not bool(user):
            raise HTTPException(status_code=401, detail="User unauthorized")        
        
        if not PasswordService.compare_password(user_auth.password, user.password):
            raise HTTPException(status_code=401, detail="User unauthorized")        
            
        token = encode({
            "name": user.name,
            "username": user.username,
            "exp": datetime.now(tz=timezone.utc) + timedelta(hours=int(os.environ.get("JWT_EXPIRE_IN")),)
        }, str(os.environ.get("JWT_SECRET")), algorithm="HS256")

        return {
            "token": token,
            "user": user
        }