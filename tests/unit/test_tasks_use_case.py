from datetime import date
from unittest.mock import AsyncMock

import pytest

from app.schemas.tasks import TaskCreate, TaskRead, TaskUpdate
from app.usecases import TasksUseCase


@pytest.fixture
def mock_tasks_repo():
    return AsyncMock()


@pytest.fixture
def tasks_use_case(mock_tasks_repo):
    return TasksUseCase(mock_tasks_repo)


@pytest.mark.asyncio
async def test_create_task(tasks_use_case, mock_tasks_repo):
    answer = 1
    mock_tasks_repo.add_one.return_value = answer
    task_data = TaskCreate(title="Fix bug in API",
                           description="Resolve issue with task filtering",
                           due_date=date(2025, 1, 15),
                           user_id=1)

    task_id = await tasks_use_case.create_task(task_data)

    assert task_id == answer
    mock_tasks_repo.add_one.assert_called_once_with(task_data.model_dump())


@pytest.mark.asyncio
async def test_get_task(tasks_use_case, mock_tasks_repo):
    task_data = {"id": 1,
                 "title": "Fix bug in API",
                 "description": "Resolve issue with task filtering",
                 "due_date": date(2025, 1, 15),
                 "user_id": 1}
    mock_tasks_repo.get_one_by_id.return_value = task_data

    task = await tasks_use_case.get_task(1)

    assert isinstance(task, TaskRead)
    assert task.id == task_data.get('id')
    assert task.title == task_data.get('title')
    assert task.description == task_data.get('description')
    assert task.due_date == task_data.get('due_date')
    assert task.user_id == task_data.get('user_id')
    mock_tasks_repo.get_one_by_id.assert_called_once_with(1)


@pytest.mark.asyncio
async def test_get_tasks(tasks_use_case, mock_tasks_repo):
    tasks_data = [
        {"id": 1,
         "title": "Fix bug in API",
         "description": "Resolve issue with task filtering",
         "due_date": date(2025, 1, 15),
         "user_id": 1},
        {"id": 2,
         "title": "Fix bug in API",
         "description": "Resolve issue with task filtering",
         "due_date": date(2025, 1, 15),
         "user_id": 2}
    ]
    mock_tasks_repo.get_list.return_value = tasks_data

    tasks = await tasks_use_case.get_tasks(user_id=1)

    assert len(tasks) == 2
    assert tasks[0].title == tasks_data[0].get('title')
    assert tasks[1].title == tasks_data[1].get('title')
    mock_tasks_repo.get_list.assert_called_once_with(user_id=1)


@pytest.mark.asyncio
async def test_update_task(tasks_use_case, mock_tasks_repo):
    mock_tasks_repo.update_one.return_value = 1
    task_update = TaskUpdate(title="Updated Title")

    updated_task_id = await tasks_use_case.update_task(1, task_update)

    assert updated_task_id == 1
    mock_tasks_repo.update_one.assert_called_once_with(1, task_update.model_dump(exclude_defaults=True))


@pytest.mark.asyncio
async def test_delete_task(tasks_use_case, mock_tasks_repo):
    mock_tasks_repo.delete_one.return_value = True

    result = await tasks_use_case.delete_task(1)

    assert result is True
    mock_tasks_repo.delete_one.assert_called_once_with(1)


@pytest.mark.asyncio
async def test_delete_task_not_found(tasks_use_case, mock_tasks_repo):
    mock_tasks_repo.delete_one.return_value = False

    with pytest.raises(ValueError, match="Task is not exist"):
        await tasks_use_case.delete_task(1)
