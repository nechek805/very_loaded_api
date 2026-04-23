from sqlalchemy.orm import Session

from src.task.models import Task
from src.task.repository import TaskRepository
from src.task.schemas import TaskCreate, TaskRead, TaskUpdate

class TaskService:
    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db)

    async def get_tasks(self) -> list[TaskRead]:
        tasks = await self.task_repository.get_tasks()
        return [TaskRead.model_validate(task) for task in tasks]
    

    async def create_task(self, task: TaskCreate) -> TaskRead:
        task_model = Task(**task.model_dump())
        created_task = await self.task_repository.create_task(task_model)
        return TaskRead.model_validate(created_task)
    
    async def get_task(self, task_id: int) -> TaskRead | None:
        task_model = await self.task_repository.get_task_by_id(task_id)
        if task_model is None:
            return None
        return TaskRead.model_validate(task_model)
    
    async def delete_task(self, task_id: int) -> TaskRead | None:
        task_model = await self.task_repository.soft_delete_task_by_id(task_id)
        if task_model is None:
            return None
        return TaskRead.model_validate(task_model)
    
    async def update_task(self, task_id, task: TaskUpdate) -> TaskRead | None:
        task_db = await self.task_repository.get_task_by_id(task_id)

        if task_db is None:
            return None
        
        if task.title is not None:
            task_db.title = task.title
        if task.start is not None:
            task_db.start = task.start
        if task.end is not None:
            task_db.end = task.end
        
        updated_task  = await self.task_repository.update_task(task_db)

        return TaskRead.model_validate(updated_task)
        