from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.task.models import Task

class TaskRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_tasks(self):
        stmt = select(Task)
        result = await self.db.scalars(stmt)
        return list(result)