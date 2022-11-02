from pydantic import BaseModel

class User(BaseModel): 
    name: str
    username: str
    password: str

class UserCreate(BaseModel): 
    name: str
    username: str
    password: str = ""

class UserUpdate(BaseModel): 
    name: str
    username: str

class UserAuth(BaseModel): 
    username: str
    password: str

class UserPayload(BaseModel): 
    name: str
    username: str