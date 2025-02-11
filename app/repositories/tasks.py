from app.interfaces import TasksRepositoryInterface
from app.models.tasks import Task
from app.repositories.base_repository import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository[Task], TasksRepositoryInterface):
    model = Task
