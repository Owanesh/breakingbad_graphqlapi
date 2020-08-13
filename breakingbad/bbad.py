import typing
import strawberry
from data import select_all
from schemas import Character, Death, Quote, Episode


def get_characters():
    return select_all("characters")


def get_deaths():
    return select_all("deaths")


def get_quotes():
    return select_all("quotes")


def get_episodes():
    return select_all("episodes")


@strawberry.type
class Query:
    characters: typing.List[Character] = strawberry.field(resolver=get_characters)
    deaths: typing.List[Death] = strawberry.field(resolver=get_deaths)
    quotes: typing.List[Quote] = strawberry.field(resolver=get_quotes)
    episodes: typing.List[Episode] = strawberry.field(resolver=get_episodes)


schema = strawberry.Schema(query=Query)
