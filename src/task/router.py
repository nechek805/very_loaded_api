from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.task.service import TaskService



router = APIRouter(prefix="/task")


@router.get("/tasks")
async def get_tasks(db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    tasks = await service.get_tasks()
    return tasks
    