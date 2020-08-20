from models import Death
from typing import List, Optional
import strawberry
from database import select_all, select_by_field
from strawberry.arguments import UNSET


@strawberry.input
class DeathFilter:
    cause: Optional[str] = UNSET
    death_id: Optional[strawberry.ID] = UNSET
    death: Optional[str] = UNSET
    cause: Optional[str] = UNSET
    responsible: Optional[str] = UNSET
    season: Optional[int] = UNSET
    number_of_deaths: Optional[int] = UNSET


@strawberry.type
class DeathsQuery:
    @strawberry.field
    def deaths(self, filters: Optional[DeathFilter] = None) -> List[Death]:
        if not filters:
            return select_all(class_map=Death)
        return select_by_field(class_map=Death, filters=filters)
