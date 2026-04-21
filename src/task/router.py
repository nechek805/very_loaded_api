from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.task.service import TaskService



router = APIRouter("/task")


@router.get("/tasks")
async def get_tasks(db: Session = Depends(get_db)):
    service = TaskService(db)
    tasks = await service.get_tasks()
    return tasks
    