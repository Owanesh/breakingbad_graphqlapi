import strawberry
from strawberry.arguments import UNSET
from typing import Optional
from models import Death, Episode, Character, Quote
from models import (
    DeathQueryResult,
    EpisodeQueryResult,
    CharacterQueryResult,
    QuoteQueryResult,
    BasicQueryResult,
)
from database import select_by_field, select_all, element_exist
from filters import DeathFilter, EpisodeFilter, QuoteFilter, CharacterFilter


def make_resolver(
    class_map: strawberry.type = None,
    Qrm: BasicQueryResult = None,  # Query Result Model
    filter_map: Optional[strawberry.type] = UNSET,
    first: Optional[int] = UNSET,
    after: Optional[strawberry.ID] = UNSET,
) -> list:
    def resolver(
        filters: Optional[filter_map] = UNSET,
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
        print("filter : ", filters)
        if not filters:
            print("no filter available")
            return Qrm(
                next=has_next,
                items=select_all(class_map=class_map, limit=first, offset=after),
            )
        return Qrm(
            next=has_next,
            items=select_by_field(
                class_map=class_map, filters=filters, limit=first, offset=after
            ),
        )

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
    ) -> DeathQueryResult:
        if responsible:
            if not filters:
                filters = DeathFilter()
            filters.responsible = make_resolver(
                class_map=Character, filter_map=responsible
            )()[0].name
        
        return make_resolver(
            class_map=Death,
            filter_map=DeathFilter,
            first=first,
            after=after,
            Qrm=DeathQueryResult,
        )()

    episodes: EpisodeQueryResult = strawberry.field(
        resolver=make_resolver(
            class_map=Episode, filter_map=EpisodeFilter, Qrm=EpisodeQueryResult
        )
    )
    characters: CharacterQueryResult = strawberry.field(
        resolver=make_resolver(
            class_map=Character, filter_map=CharacterFilter, Qrm=CharacterQueryResult
        )
    )
    quotes: QuoteQueryResult = strawberry.field(
        resolver=make_resolver(
            class_map=Quote, filter_map=QuoteFilter, Qrm=QuoteQueryResult
        )
    )


schema = strawberry.Schema(query=Query)
