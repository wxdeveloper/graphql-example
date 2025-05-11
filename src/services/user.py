from typing import Dict, List


users: Dict[str, Dict] = {
    "1": {"id": "1", "name": "Петя"},
    "2": {"id": "2", "name": "Ваня"},
}

def list_users() -> List[Dict]:
    return list(users.values())

def get_user(user_id: str) -> Dict:
    return users.get(user_id)
