from sqlalchemy.orm import Session

from src.task.repository import TaskRepository

class TaskService:
    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db)

    async def get_tasks(self):
        return self.task_repository.get_tasks()