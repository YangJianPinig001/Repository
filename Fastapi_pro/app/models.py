import uuid

from sqlmodel import Relationship, Field, SQLModel



class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: list["Hero"] = Relationship(back_populates="team")

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    full_name: str | None = None
    disabled: bool = False
    hashed_password: str | None = None

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"