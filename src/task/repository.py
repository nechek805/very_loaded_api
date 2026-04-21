from sqlalchemy import select
from sqlalchemy.orm import Session

from src.task.models import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    async def get_tasks(self):
        stmt = select(Task)
        return list(self.db.scalars(stmt))