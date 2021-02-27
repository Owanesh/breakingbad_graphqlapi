import strawberry
from strawberry.arguments import UNSET
import typing
from models import Death, Episode, Character, Quote
from database import select_by_field, select_all, element_exist
from filters import DeathFilter, EpisodeFilter, QuoteFilter, CharacterFilter


def make_resolver(
    class_map: strawberry.type = None,
    filter_map: strawberry.type = UNSET,
    first: typing.Optional[int] = None,
    after: typing.Optional[strawberry.ID] = None,
) -> list:
    def resolver(filters: filter_map = None):
        if not filters:
            return select_all(class_map=class_map, limit=first, offset=after)
        return select_by_field(
            class_map=class_map, filters=filters, limit=first, offset=after
        )

    return resolver


@strawberry.type
class Query:
    @strawberry.field
    def deaths(
        self,
        info,
        filters: typing.Optional[DeathFilter] = None,
        responsible: typing.Optional[CharacterFilter] = None,
        first: typing.Optional[int] = None,
        after: typing.Optional[strawberry.ID] = None,
    ) -> Death.QueryResult:
        if responsible:
            if not filters:
                filters: CharacterFilter = CharacterFilter()
            filters.responsible = make_resolver(
                class_map=Character, filter_map=responsible
            )()[0].name
        has_next = (
            (int(after) + first)
            if element_exist(class_map=Death, identifier=int(after) + first)
            else -1
        )
        return Death.QueryResult(
            has_next, make_resolver(class_map=Death, first=first, after=after)()
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
