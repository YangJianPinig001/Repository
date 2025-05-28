from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.models import Hero,Team, User
from app.schemas import HeroPublic, HeroCreate, UserCreate, UserPublic
from sqlmodel import Session, select
from app.db import engine
from app.dependencies import get_session

router = APIRouter()


def hash_password(password):
    # hash加密
    return password


@router.post("/users/", response_model=UserPublic)
async def create_user(*, session: Session = Depends(get_session), user: UserCreate):
    exist_user = session.exec(select(User).where(User.email == user.email)).first()
    if exist_user:
        raise HTTPException(status_code=400, detail="邮件账号已存在")
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        disabled=user.disabled,
        hashed_password=hash_password(user.password)
    )
    session.add(user)
    return db_user


@router.post("/heroes/", response_model=HeroPublic, tags=["users"])
async def create_heroes(*, session: Session = Depends(get_session), hero: HeroCreate):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@router.get("/heroes/", tags=["users"], response_model=List[HeroPublic])
async def get_heroes(*, session: Session = Depends(get_session)):
    statement = select(Hero)
    heroes = session.exec(statement).all()
    return heroes

@router.get("/update/me")
async def update_heroes():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        session.add(team_preventers)
        session.add(team_z_force)
        session.commit()

        hero_deadpond = Hero(
            name="Deadpond", secret_name="Dive Wilson", team_id=team_z_force.id
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            team_id=team_preventers.id,
        )
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()
    return {"message": "Hero updated successfully"}


@router.get("/heroes/{hero_id}", response_model=HeroPublic)
async def query_hero(*, hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="heroes not found")
    return hero


@router.delete("/heroes/{hero_id}")
async def query_hero(*, hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    session.delete(hero)
    session.commit()
    return []