from __future__ import annotations
from typing import List
import strawberry
from database import select_by_field, _select_character_by_name
from filters import CharacterFilter
import ast


def lit_eval(param: str) -> List:
    return ast.literal_eval(param)



@strawberry.type
class Character:
    __tablename__ = "characters"
    char_id: strawberry.ID
    name: str
    birthday: str
    occupation: str
    img: str
    status: str
    nickname: str
    portrayed: str
    serie: str
    season_appearance: str


@strawberry.type
class Episode:
    __tablename__ = "episodes"
    episode_id: strawberry.ID
    title: str
    season: int
    episode: int
    air_date: str
    series: str
    characters: List[str]

    @strawberry.field
    def characters(self, info) -> List[Character]:
        return _select_character_by_name(Character, list_of_names = lit_eval(self.characters))



@strawberry.type
class Quote:
    __tablename__ = "quotes"
    quote_id: strawberry.ID
    quote: str
    series: str
    author_id: int
   
    @strawberry.field
    def author(self, info) -> Character:
        return select_by_field(Character, CharacterFilter(self.author_id))[0]


@strawberry.type
class Death:
    __tablename__ = "deaths"
    death_id: strawberry.ID
    death: str
    cause: str
    season: int
    episode: int
    number_of_deaths: int
    last_words: str
    responsible: str

    # Dont' use this
    # @strawberry.field
    # def responsible(self, info) -> Character:
    #     return select_by_field(Character, CharacterFilter(name=self.responsible))[0]
