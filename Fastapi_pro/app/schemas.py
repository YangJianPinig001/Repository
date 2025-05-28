import uuid

from sqlmodel import SQLModel
from typing import Optional, List

class TeamBase(SQLModel):
    name: str
    headquarters: str

class TeamCreate(TeamBase):
    pass

class TeamPublic(TeamBase):
    id: int

class TeamUpdate(SQLModel):
    name: Optional[str] = None
    headquarters: Optional[str] = None

class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None
    team_id: Optional[int] = None

class HeroCreate(HeroBase):
    pass

class HeroPublic(HeroBase):
    id: int

class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[int] = None

class HeroPublicWithTeam(HeroPublic):
    """返回数据包含一个TeamPublic对象"""
    team: Optional[TeamPublic] = None

class TeamPublicWithHeroes(TeamPublic):
    """返回数据包含一个HeroPublic列表"""
    heroes: List[HeroPublic] = []


class UserBase(SQLModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: bool = False

class UserCreate(UserBase):
    password: str

class UserPublic(UserBase):
    id: uuid.UUID