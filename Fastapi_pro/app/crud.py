from typing import List, Optional
from sqlmodel import Session, select
from app.models import Hero, Team



def create_hero(session: Session, hero: Hero) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

def get_hero(session: Session, hero_id: int) -> Optional[Hero]:
    return session.get(Hero, hero_id)

def get_heroes(session: Session, offset: int = 0, limit: int = 100) -> List[Hero]:
    statement = select(Hero).offset(offset).limit(limit)
    return session.exec(statement).all()

def update_hero(session: Session, hero_id: int, hero_data: dict) -> Optional[Hero]:
    db_hero = session.get(Hero, hero_id)
    if not db_hero:
        return None
    for key, value in hero_data.items():
        setattr(db_hero, key, value)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

def delete_hero(session: Session, hero_id: int) -> bool:
    db_hero = session.get(Hero, hero_id)
    if not db_hero:
        return False
    session.delete(db_hero)
    session.commit()
    return True

# Team CRUD

def create_team(session: Session, team: Team) -> Team:
    session.add(team)
    session.commit()
    session.refresh(team)
    return team

def get_team(session: Session, team_id: int) -> Optional[Team]:
    return session.get(Team, team_id)

def get_teams(session: Session, offset: int = 0, limit: int = 100) -> List[Team]:
    statement = select(Team).offset(offset).limit(limit)
    return session.exec(statement).all()

def update_team(session: Session, team_id: int, team_data: dict) -> Optional[Team]:
    db_team = session.get(Team, team_id)
    if not db_team:
        return None
    for key, value in team_data.items():
        setattr(db_team, key, value)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team

def delete_team(session: Session, team_id: int) -> bool:
    db_team = session.get(Team, team_id)
    if not db_team:
        return False
    session.delete(db_team)
    session.commit()
    return True