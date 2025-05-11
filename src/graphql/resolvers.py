from typing import List, Optional
import strawberry
from src.services.user import list_users, get_user, users
from src.graphql.types import User

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        return [User(id=u['id'], name=u['name']) for u in list_users()]

    @strawberry.field
    def user(self, id: strawberry.ID) -> Optional[User]:
        u = get_user(str(id))
        if not u:
            return None
        return User(id=u['id'], name=u['name'])


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(
        self,
        id: strawberry.ID,
        name: str,
    ) -> User:
        users.update({'id': id, 'name': name})
        print(users)
        return User(id=id, name=name)