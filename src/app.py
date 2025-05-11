from fastapi import FastAPI
from src.graphql.schema import graphql_app


app = FastAPI(title='graphql')
app.include_router(graphql_app, prefix='/graphql')