from unittest.mock import AsyncMock

import pytest

from app.schemas.users import UserCreate, UserRead
from app.usecases import UsersUseCase


@pytest.fixture
def mock_users_repo():
    return AsyncMock()


@pytest.fixture
def users_use_case(mock_users_repo):
    return UsersUseCase(mock_users_repo)


@pytest.mark.asyncio
async def test_register_user(users_use_case, mock_users_repo):
    answer = 1
    mock_users_repo.add_one.return_value = answer
    user_data = UserCreate(username="john_doe", email="john@example.com")

    user_id = await users_use_case.register_user(user_data)

    assert user_id == answer
    mock_users_repo.add_one.assert_called_once_with(user_data.model_dump())


@pytest.mark.asyncio
async def test_get_user(users_use_case, mock_users_repo):
    user_data = {"id": 1, "username": "john_doe", "email": "john@example.com"}
    mock_users_repo.get_one_by_id.return_value = user_data

    user = await users_use_case.get_user(1)

    assert isinstance(user, UserRead)
    assert user.id == user_data.get('id')
    assert user.username == user_data.get('username')
    assert user.email == user_data.get('email')
    mock_users_repo.get_one_by_id.assert_called_once_with(1)

