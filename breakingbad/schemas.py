from __future__ import annotations
import typing
import strawberry


@strawberry.type
class Character:
    id: int
    name: str
    birthday: str
    occupation: typing.List[str]
    img: str
    status: str
    nickname: str
    appearance: typing.List[int]
    portrayed: str
    category: typing.List[str]


@strawberry.type
class Episode:
    id: int
    title: str
    season: int 
    episode: int 
    air_date: str 
    characters: typing.List[Character]
    series: str


@strawberry.type
class Quote:
    id: int
    quote: str
    author: str
    series: str


@strawberry.type
class Death:
    id: int
    death: str
    cause: str
    responsible: str
    last_word: str
    season: int
    episode: Episode
    number_of_deaths: int