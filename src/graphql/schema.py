import strawberry
from strawberry.fastapi import GraphQLRouter
from src.graphql.resolvers import Query, Mutation


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(
    schema,
    graphql_ide="graphiql",
    allow_queries_via_get=True,
)