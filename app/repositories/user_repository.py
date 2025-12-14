from typing import List, Optional
from app.models.user import User

class UserRepository:
    def __init__(self) -> None:
        self._users: List[User] = []
    
    def add(self, user: User) -> None:
        self._users.append(user)

    def get_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self._users if u.id == user_id), None)
    
    def get_all(self) -> List[User]:
        return self._users