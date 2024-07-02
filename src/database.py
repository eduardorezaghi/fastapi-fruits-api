from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src import database

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:postgres@db:5432/fruits_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@lru_cache
def create_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.destroy()


def get_session():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
