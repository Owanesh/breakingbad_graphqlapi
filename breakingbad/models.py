from __future__ import annotations
from typing import List
import strawberry


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
    appearance: List[int]
    portrayed: str
    category: List[str]


@strawberry.type
class Episode:
    __tablename__ = "episodes"
    episode_id: strawberry.ID
    title: str
    season: int
    episode: int
    air_date: str
    characters: List[Character]
    series: str


@strawberry.type
class Quote:
    __tablename__ = "quotes"
    quote_id: strawberry.ID
    quote: str
    author: str
    series: str


@strawberry.type
class Death:
    __tablename__ = "deaths"
    death_id: strawberry.ID
    death: str
    cause: str
    responsible: str
    last_word: str
    season: int
    episode: Episode
    number_of_deaths: int
