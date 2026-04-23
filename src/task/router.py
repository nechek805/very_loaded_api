from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.task.service import TaskService
from src.task.schemas import TaskCreate, TaskRead, TaskUpdate



router = APIRouter(prefix="/tasks", tags=["task"])


@router.get("/")
async def get_tasks(db: AsyncSession = Depends(get_db)) -> list[TaskRead]:
    service = TaskService(db)
    tasks = await service.get_tasks()
    return tasks
    

@router.post("/")
async def create_task(
    task: TaskCreate, 
    db: AsyncSession = Depends(get_db)
) -> TaskRead:
    service = TaskService(db)
    task = await service.create_task(task)
    return task


@router.get("/{task_id}")
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
) -> TaskRead:
    service = TaskService(db)
    task = await service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
) -> None:
    service = TaskService(db)
    deleted = await service.delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found") 
    

@router.patch("/{task_id}")
async def update_task(
    task_id,
    task: TaskUpdate,
    db: AsyncSession = Depends(get_db)
) -> TaskRead:
    service = TaskService(db)
    task = await service.update_task(task_id, task)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task