from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.task.models import Task

class TaskRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_tasks(self) -> list[Task]:
        stmt = select(Task).where(Task.is_active.is_(True))
        result = await self.db.scalars(stmt)
        return list(result)
    
    async def create_task(self, task: Task) -> Task:
        self.db.add(task)
        await self.db.commit()
        await self.db.refresh(task)
        return task
    
    async def get_task_by_id(self, task_id: int) -> Task:
        stmt = select(Task).where(
            Task.id == task_id, 
            Task.is_active.is_(True)
            )
        result = await self.db.scalar(stmt)
        return result
    
    async def soft_delete_task_by_id(self, task_id: int) -> Task | None:
        task = await self.get_task_by_id(task_id)

        if task is None:
            return None
        
        task.is_active = False
        await self.db.commit()
        await self.db.refresh(task)
        return task
    
    async def update_task(self, task: Task) -> Task:
        await self.db.commit()
        await self.db.refresh(task)
        return task
