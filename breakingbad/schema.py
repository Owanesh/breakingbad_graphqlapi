from __future__ import annotations
from typing import List, Optional, Generic, TypeVar
import strawberry
from database import select_by_field, _select_character_by_name
from filters import CharacterFilter
from strawberry.arguments import UNSET


@strawberry.interface
class BasicModel:
    __tablename__: str


T = TypeVar("T")


@strawberry.type
class QueryResult(Generic[T]):
    items: Optional[List[Optional[T]]]
    next: Optional[strawberry.ID] = UNSET


@strawberry.type
class Character(BasicModel):
    __tablename__ = "characters"
    char_id: strawberry.ID
    name: str
    birthday: str
    occupation: List[str]
    img: str
    status: str
    nickname: str
    portrayed: str
    serie: str
    season_appearance: List[int]

    def identifier():
        return Character.char_id


@strawberry.type
class Episode(BasicModel):
    __tablename__ = "episodes"
    episode_id: strawberry.ID
    title: str
    season: int
    episode: int
    air_date: str
    series: str
    characters_name: List[str]

    def identifier():
        return Episode.episode_id

    @strawberry.field
    def characters(self, info) -> List[Character]:
        return _select_character_by_name(Character, self.characters_name)


@strawberry.type
class Quote(BasicModel):
    __tablename__ = "quotes"
    quote_id: strawberry.ID
    quote: str
    series: str
    author_id: int

    def identifier():
        return Quote.quote_id

    @strawberry.field
    def author(self, info) -> Character:
        return select_by_field(Character, CharacterFilter(self.author_id))[0]


@strawberry.type
class Death(BasicModel):
    __tablename__ = "deaths"
    death_id: strawberry.ID
    death: str
    cause: str
    season: int
    episode: int
    number_of_deaths: int
    last_words: str
    responsible: str

    def identifier():
        return Death.death_id
