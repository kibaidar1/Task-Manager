from typing import Annotated
from fastapi import Depends

from app.database import get_async_session, async_session_maker
from app.repositories.tasks import TasksRepository
from app.repositories.users import UsersRepository
from app.usecases import UsersUseCase, TasksUseCase


users_use_case = UsersUseCase(UsersRepository(async_session_maker()))
tasks_use_case = TasksUseCase(TasksRepository(async_session_maker()))


def get_users_use_case():
    return users_use_case


def get_tasks_use_case():
    return tasks_use_case


UsersUseCaseDep = Annotated[UsersUseCase, Depends(get_users_use_case)]
TasksUseCaseDep = Annotated[TasksUseCase, Depends(get_tasks_use_case)]

