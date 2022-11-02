from app.services.database import conn
from app.services.password import PasswordService
from app.models.user import users
from app.schemas.user import UserCreate, UserUpdate

class UserService:
    def login(self, username: str):
        return conn.execute(users.select().where(users.c.username == username)).first()
    
    def findAll(self):
        return conn.execute(users.select()).fetchall()
    
    def findOne(self, id: int):
        return conn.execute(users.select().where(users.c.id == id)).fetchall()
    
    def create(self, user: UserCreate):
        password = PasswordService.hash_password(user.password)
        conn.execute(users.insert().values(
            name=user.name, 
            username=user.username, 
            password=password
        ))
        return conn.execute(users.select()).fetchall()
    
    def update(self, id: int, user: UserUpdate):
        conn.execute(users.update().values(
            name=user.name, 
            username=user.username,
        ).where(users.c.id == id))
        return conn.execute(users.select()).fetchall()
    
    def delete(self, id: int):
        conn.execute(users.delete().where(users.c.id == id))
        return conn.execute(users.select()).fetchall()