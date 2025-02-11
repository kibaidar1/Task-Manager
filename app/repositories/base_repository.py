from typing import TypeVar, Generic, Type, AsyncGenerator

from sqlalchemy import insert, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.interfaces import BaseRepositoryInterface


T = TypeVar("T", bound=DeclarativeBase)


class SQLAlchemyRepository(BaseRepositoryInterface, Generic[T]):
    model: Type[T]

    def __init__(self, session: AsyncGenerator[AsyncSession, None]):
        self.session = session

    async def add_one(self, data: dict) -> str:
        async with self.session as session:
            stmt = insert(self.model).values(**data).returning(getattr(self.model, 'id'))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete_one(self, instance_id: int) -> bool:
        async with self.session as session:
            stmt = delete(self.model).where(self.model.id == instance_id)
            res = await session.execute(stmt)
            await session.commit()
            return True if res.rowcount else False

    async def get_one_by_id(self, instance_id: int) -> dict:
        async with self.session as session:
            stmt = select(self.model).where(self.model.id == instance_id)
            res = await session.execute(stmt)
            return res.scalar_one() if res else None

    async def get_list(self,  **filter_by,) -> list[dict]:
        async with self.session as session:
            query = select(self.model).filter_by(**filter_by)
            res = await session.execute(query)
            return res.unique().scalars().all() if res else []

    async def update_one(self, instance_id: int, data: dict) -> str:
        async with self.session as session:
            stmt = (update(self.model)
                    .where(self.model.id == instance_id)
                    .values(**data)
                    .returning(getattr(self.model, 'id')))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
