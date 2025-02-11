import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.fixture
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_register_user(async_client: AsyncClient):
    user_data = {"id": 1, "username": "john_doe", "email": "john@example.com"}
    response = await async_client.post("/users/", json=user_data)
    assert response.status_code == 303


@pytest.mark.asyncio
async def test_get_user(async_client: AsyncClient):
    response = await async_client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


@pytest.mark.asyncio
async def test_create_task(async_client: AsyncClient):
    """Тест создания задачи"""
    response = await async_client.post("/tasks/", json={"title": "New Task", "description": "Task desc", "user_id": 1})
    assert response.status_code == 303


@pytest.mark.asyncio
async def test_get_tasks(async_client: AsyncClient):
    """Тест получения всех задач"""
    response = await async_client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_update_task(async_client: AsyncClient):
    """Тест обновления задачи"""
    response = await async_client.patch("/tasks/1", json={"title": "Updated Title"})
    assert response.status_code == 303


@pytest.mark.asyncio
async def test_delete_task(async_client: AsyncClient):
    """Тест удаления задачи"""
    response = await async_client.delete("/tasks/1")
    assert response.status_code == 204