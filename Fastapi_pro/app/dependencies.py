from typing import Annotated

from fastapi import Depends
from sqlmodel import Session
from app.db import get_engine

from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")



def get_session():
    with Session(get_engine()) as session:
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise


SessionDep = Annotated[Session, Depends(get_session)]