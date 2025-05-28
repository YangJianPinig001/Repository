from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models import Hero
from app.db import engine

router = APIRouter()

@router.get("/auth/login", tags=["auth"])
async def login():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        heroes = session.exec(statement).all()
    return heroes


@router.get("/hero/{hero_id}", tags=["auth"])
def read_hero(hero_id: int):
    with Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        return hero


@router.patch("/heroes/{hero_id}", tags=["auth"])
def update_hero(hero_id: int, hero: Hero):
    with Session(engine) as session:
        db_hero = session.get(Hero, hero_id)
        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        hero_data = hero.model_dump(exclude_unset=True)
        db_hero.sqlmodel_update(hero_data)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero