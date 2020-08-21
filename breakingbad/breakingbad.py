import strawberry
import typing
from models import Death, Episode, Character, Quote
from database import select_by_field, select_all
from filters import DeathFilter, EpisodeFilter, QuoteFilter, CharacterFilter


def make_resolver(
    class_map: strawberry.type = None, filter_map: strawberry.type = None
) -> list:
    def resolver(self, filters: filter_map = None) -> str:
        if not filters:
            return select_all(class_map=class_map)
        return select_by_field(class_map=class_map, filters=filters)

    return resolver


@strawberry.type
class Query:
    deaths: typing.List[Death] = strawberry.field(
        resolver=make_resolver(class_map=Death, filter_map=DeathFilter)
    )
    episodes: typing.List[Episode] = strawberry.field(
        resolver=make_resolver(class_map=Episode, filter_map=EpisodeFilter)
    )
    characters: typing.List[Character] = strawberry.field(
        resolver=make_resolver(class_map=Character, filter_map=CharacterFilter)
    )
    quotes: typing.List[Quote] = strawberry.field(
        resolver=make_resolver(class_map=Quote, filter_map=QuoteFilter)
    )


schema = strawberry.Schema(query=Query)
