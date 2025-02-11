from app.interfaces import UsersRepositoryInterface
from app.models.users import User
from app.repositories.base_repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository[User], UsersRepositoryInterface):
    model = User
