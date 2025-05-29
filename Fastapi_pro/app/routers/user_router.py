from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.models import Hero,Team, User
from app.schemas import HeroPublic, HeroCreate, UserCreate, UserPublic
from sqlmodel import Session, select
from app.db import engine
from app.dependencies import get_session, SessionDep

router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


def hash_password(password):
    # hash加密
    return password


@router.post("/users/", response_model=UserPublic)
async def create_user(*, session: SessionDep, user: UserCreate):
    exist_user = session.exec(select(User).where(User.email == user.email)).first()
    if exist_user:
        raise HTTPException(status_code=400, detail="邮件账号已存在")
    # hero_data = hero.model_dump(exclude_unset=True)
    # hero_db.sqlmodel_update(hero_data)
    user_dict = user.model_dump()
    user_dict["hashed_password"] = hash_password(user.password)
    db_user = User(**user_dict)
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