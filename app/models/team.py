from typing import Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.hero import Hero


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list['Hero'] = Relationship(back_populates='team')
