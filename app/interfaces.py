import abc


class BaseRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    async def add_one(self, data: dict) -> int:
        ...

    @abc.abstractmethod
    async def delete_one(self, instance_id: int) -> bool:
        ...

    @abc.abstractmethod
    async def get_one_by_id(self, instance_id: int) -> dict:
        ...

    @abc.abstractmethod
    async def get_list(self, **filter_by) -> list[dict]:
        ...

    @abc.abstractmethod
    async def update_one(self, instance_id: int, data: dict) -> int:
        ...


class UsersRepositoryInterface(BaseRepositoryInterface, abc.ABC):
    ...


class TasksRepositoryInterface(BaseRepositoryInterface, abc.ABC):
    ...
