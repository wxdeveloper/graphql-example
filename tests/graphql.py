from fastapi.testclient import TestClient
from src.app import app


client = TestClient(app)


def test_get_users():
    query = """
    query {
        user(id: 2) {
            name
        }
    }
    """
    res = client.post('/graphql', json={'query': query})
    assert res.status_code == 200

def test_create_user():
    mutation = """
    mutation {
        createUser(id: "123", name: "Петя") {
            id,
            name
        }
    }
    """
    res = client.post('/graphql', json={'query': mutation})
    assert res.status_code == 200



if __name__ == '__main__':
    test_create_user()