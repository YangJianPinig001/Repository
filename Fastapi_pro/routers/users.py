from fastapi import APIRouter
from Fastapi_pro.models import Hero, Team
from sqlmodel import Session, select
from Fastapi_pro.db import engine

router = APIRouter()


@router.get("/test/me")
async def create_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        h = session.exec(statement).first()
        t = h.team
    return t

@router.get("/test/query", tags=["users"])
async def create_heroes():
    with Session(engine) as session:
        statement = select(Hero).join(Team, isouter=True).where(Team.name == "Preventers")
        results = session.exec(statement)
        for hero in results:
            print("Hero:", hero)
    return "successfully created heroes"

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


@router.get("/select")
async def select_heroes():
    with Session(engine) as session:
        statement = select(Hero, Team).where(Hero.team_id == Team.id)
        results = session.exec(statement).all()
        serialized = [
            {
                "hero": hero.model_dump(),
                "team": team.model_dump()
            }
            for hero, team in results
        ]

    return serialized