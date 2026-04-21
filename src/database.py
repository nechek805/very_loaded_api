from sqlalchemy.orm import DeclarativeBase, Session
from contextlib import contextmanager
from sqlalchemy import create_engine

import os


class Base(DeclarativeBase):
    pass



DATABASE_URL=os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set in env")

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
    )



@contextmanager
def get_db():
    with Session(engine) as session:
        try:
            yield session   
            session.commit()
        except Exception:
            session.rollback()
            raise