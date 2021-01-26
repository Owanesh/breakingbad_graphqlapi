from __future__ import annotations
from typing import List
import strawberry
from database import select_by_field, metadata
from filters import CharacterFilter
from sqlalchemy import Table, Column, Integer, String,  JSON 
from sqlalchemy.orm import mapper
 

@strawberry.type
class Character:
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


character_tbl = Table(
    Character.__tablename__,
    metadata,
    Column("char_id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("birthday", String(10)),
    Column("occupation", JSON),
    Column("img", String(200)),
    Column("status", String(15)),  # at least "presumed dead"
    Column("nickname", String(40)),
    Column("portrayed", String(50)),
    Column("serie", String(30)),
    Column("season_appearance", JSON),
    Column("better_call_saul_appearance", JSON),
)

mapper(Character, character_tbl)


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

"""
    @strawberry.field
    def characters(self, info) -> List[Character]:
        # import pdb; pdb.set_trace()
        return _select_character_by_name(
            Character, list_of_names=lit_eval(self.characters)
        )
"""


episode_tbl = Table(
    Episode.__tablename__,
    metadata,
    Column("episode_id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("season", Integer),
    Column("episode", Integer),
    Column("air_date", String(200)),
    Column("series", String(35)),
    Column("characters", JSON),
)

mapper(Episode, episode_tbl)


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


quote_tbl = Table(
    Quote.__tablename__,
    metadata,
    Column("quote_id", Integer, primary_key=True),
    Column("quote", String(50)),
    Column("author_id", Integer),
    Column("series", String(35)),
)

mapper(Quote, quote_tbl)


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


death_tbl = Table(
    Death.__tablename__,
    metadata,
    Column("death_id", Integer, primary_key=True),
    Column("death", String(50)),
    Column("cause", String(50)),
    Column("season", Integer),
    Column("episode", Integer),
    Column("number_of_deaths", Integer),
    Column("last_words", String(35)),
    Column("responsible", String(35)),
)

mapper(Death, death_tbl)