from typing import List, Optional
import strawberry
from strawberry.arguments import UNSET


@strawberry.input
class DeathFilter:
    death_id: Optional[strawberry.ID] = UNSET
    cause: Optional[str] = UNSET
    death: Optional[str] = UNSET
    cause: Optional[str] = UNSET
    responsible: Optional[str] = UNSET
    season: Optional[int] = UNSET
    number_of_deaths: Optional[int] = UNSET


@strawberry.input
class EpisodeFilter:
    episode_id: Optional[strawberry.ID] = UNSET
    title: Optional[str] = UNSET
    season: Optional[int] = UNSET
    episode: Optional[int] = UNSET
    air_date: Optional[str] = UNSET
    series: Optional[str] = UNSET


@strawberry.input
class QuoteFilter:
    quote_id: Optional[strawberry.ID] = UNSET
    quote: Optional[str] = UNSET
    author: Optional[str] = UNSET
    series: Optional[str] = UNSET


@strawberry.input
class CharacterFilter:
    char_id: Optional[strawberry.ID] = UNSET
    name: Optional[str] = UNSET
    birthday: Optional[str] = UNSET
    status: Optional[str] = UNSET
    nickname: Optional[str] = UNSET
    portrayed: Optional[str] = UNSET
