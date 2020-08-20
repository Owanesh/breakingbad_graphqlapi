import strawberry
from schema import DeathsQuery


@strawberry.type
class Query(DeathsQuery):
    pass


schema = strawberry.Schema(query=Query)
