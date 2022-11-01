from app.services.database import conn
from app.models.user import users
from app.schemas.user import User

class UserService:
    def findAll(self):
        return conn.execute(users.select()).fetchall()
    
    def findOne(self, id: int):
        return conn.execute(users.select().where(users.c.id == id)).fetchall()
    
    def create(self, user: User):
        conn.execute(users.insert().values(
            name=user.name, 
            username=user.username, 
            password=user.password
        ))
        return conn.execute(users.select()).fetchall()
    
    def update(self, id: int, user: User):
        conn.execute(users.update().values(
            name=user.name, 
            username=user.username, 
            password=user.password
        ).where(users.c.id == id))
        return conn.execute(users.select()).fetchall()
    
    def delete(self, id: int):
        conn.execute(users.delete().where(users.c.id == id))
        return conn.execute(users.select()).fetchall()