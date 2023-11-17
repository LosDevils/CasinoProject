from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update, select
from src.database.base import Base


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, id: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None
    adapter = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> Base:
        stmt = insert(self.model).values(**data).returning(self.model)
        result = await self.session.execute(stmt)
        return self.adapter.to_domain_model(orm_model=result.scalar_one())

    async def edit_one(self, id: int, data: dict) -> Base:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        result = await self.session.execute(stmt)
        return self.adapter.to_domain_model(result.scalar_one())

    async def find_one(self, **filter_by) -> Base:
        stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        result = self.adapter.to_domain_model(result.scalar_one())
        return result

    async def find_all(self, **filter_by) -> list:
        stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        result = [self.adapter.to_domain_model(row[0]) for row in result.all()]
        return result
