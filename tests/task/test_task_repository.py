import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta

from src.task.models import Task
from src.task.repository import TaskRepository




@pytest.mark.asyncio
async def test_get_tasks(db_session: AsyncSession):
    now = datetime.now()
    db_session.add_all([
        Task(
            title="Test task 1",
            start=now,
            end = now + timedelta(minutes=1),
        ),
        Task(
            title="Test task 2",
            start=now,
            end = now + timedelta(minutes=3),
            is_active = False,
        )
    ])

    repo = TaskRepository(db_session)
    result = await repo.get_tasks()

    assert len(result) == 2
    assert result[0].title == "Test task 1"
    assert result[0].start == now
    assert result[0].end == now + timedelta(minutes=1)
    assert result[0].is_active == True #noqa: E712
    assert result[1].is_active == False #noqa: E712
