import os
from sqlalchemy import MetaData, create_engine

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")

engine = create_engine(f"mysql://{DB_USER}:{DB_PASS}@127.0.0.1/{DB_NAME}")

meta = MetaData()

conn = engine.connect()