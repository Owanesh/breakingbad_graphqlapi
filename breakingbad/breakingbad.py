import strawberry
from strawberry.arguments import UNSET
from typing import Optional, Type
from models import Death, Episode, Character, Quote
from schema import QueryResult
from database import select_by_field, select_all, element_exist
from filters import DeathFilter, EpisodeFilter, QuoteFilter, CharacterFilter


def make_resolver(
    class_map: Type,
    filter_type: Type,
) -> list:
    def resolver(
        filters: Optional[filter_type] = UNSET,
        first: Optional[int] = UNSET,
        after: Optional[strawberry.ID] = UNSET,
    ):
        has_next = (
            (
                (int(after) + first)
                if element_exist(class_map=class_map, identifier=int(after) + first)
                else 0
            )
            if after
            else 0
        )

        items = (
            select_all(class_map=class_map, limit=first, offset=after)
            if not filters
            else select_by_field(
                class_map=class_map, filters=filters, limit=first, offset=after
            )
        )

        return QueryResult(next=has_next, items=items)

    return resolver


@strawberry.type
class Query:
    @strawberry.field
    def deaths(
        self,
        info,
        filters: Optional[DeathFilter] = UNSET,
        responsible: Optional[CharacterFilter] = UNSET,
        first: Optional[int] = UNSET,
        after: Optional[strawberry.ID] = UNSET,
    ) -> QueryResult[Death]:
        if responsible:
            if not filters:
                filters = DeathFilter()
            filters.responsible = select_by_field(
                class_map=Character, filters=responsible
            )[0].name

        return make_resolver(Death, DeathFilter)(filters, first, after)

    episodes: QueryResult[Episode] = strawberry.field(
        resolver=make_resolver(Episode, EpisodeFilter)
    )
    characters: QueryResult[Character] = strawberry.field(
        resolver=make_resolver(Character, CharacterFilter)
    )
    quotes: QueryResult[Quote] = strawberry.field(
        resolver=make_resolver(Quote, QuoteFilter)
    )


schema = strawberry.Schema(query=Query)
