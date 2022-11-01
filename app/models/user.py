from sqlalchemy import Column, Integer, String, Table
from app.services.database import meta

users = Table(
    'user',
    meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255)),
    Column('username', String(255)),
    Column('password', String(255))
)

    
    
    
    