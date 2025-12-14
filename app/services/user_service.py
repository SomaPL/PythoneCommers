from app.models.user import User
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def create_user(self, user_id: int, email: str, name:str) -> User:
        user = User(id=user_id, email=email, name=name)
        self._user_repository.add(user)
        return user
    
    def get_user(self, user_id: int) -> User | None:
        return self._user_repository.get_by_id(user_id)
