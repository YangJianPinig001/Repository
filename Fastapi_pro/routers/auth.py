from fastapi import APIRouter
from sqlmodel import Session, select
from Fastapi_pro.models import Hero
from Fastapi_pro.db import engine

router = APIRouter()

@router.get("/auth/login", tags=["auth"])
async def login():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        heroes = session.exec(statement).all()
    return heroes