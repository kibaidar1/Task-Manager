from app.interfaces import UsersRepositoryInterface, TasksRepositoryInterface
from app.schemas.tasks import TaskCreate, TaskRead, TaskUpdate
from app.schemas.users import UserCreate, UserRead


class UsersUseCase:
    def __init__(self, user_repository: UsersRepositoryInterface):
        self._user_repository = user_repository

    async def get_user(self, user_id: int) -> UserRead:
        user = await self._user_repository.get_one_by_id(user_id)
        return UserRead.model_validate(user)

    async def register_user(self, user: UserCreate) -> int:
        user_id = await self._user_repository.add_one(user.model_dump())
        return user_id


class TasksUseCase:
    def __init__(self, tasks_repository: TasksRepositoryInterface):
        self._tasks_repository = tasks_repository

    async def create_task(self, task: TaskCreate) -> int:
        task_id = await self._tasks_repository.add_one(task.model_dump())
        return task_id

    async def delete_task(self, task_id: int) -> bool:
        res = await self._tasks_repository.delete_one(task_id)
        if not res:
            raise ValueError("Task is not exist")
        return res

    async def get_task(self, task_id: int) -> TaskRead:
        task = await self._tasks_repository.get_one_by_id(task_id)
        return TaskRead.model_validate(task) if task else None

    async def get_tasks(self, user_id: int = None) -> list[TaskRead]:
        kwargs = {}
        if user_id:
            kwargs['user_id'] = user_id
        tasks = await self._tasks_repository.get_list(**kwargs)
        return [TaskRead.model_validate(task) for task in tasks]

    async def update_task(self, task_id: int, task: TaskUpdate) -> int:
        task_id = await self._tasks_repository.update_one(task_id,
                                                          task.model_dump(exclude_defaults=True))
        return task_id


