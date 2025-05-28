from sqlmodel import Session
from app.db import get_engine


def get_session():
    with Session(get_engine()) as session:
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise