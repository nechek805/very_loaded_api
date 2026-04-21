from httpx import AsyncClient, ASGITransport
import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta

from src.core.database import get_db
from src.task.models import Task
from src.main import app


@pytest.mark.asyncio
async def test_main(client, db_session):
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
    await db_session.commit()

    response = await client.get("/task/tasks")

    assert response.status_code == 200

    result = response.json()
    assert len(result) == 2
    assert result[0]["title"] == "Test task 1"
    assert datetime.fromisoformat(result[0]["start"]) == now
    assert datetime.fromisoformat(result[0]["end"]) == now + timedelta(minutes=1)
    assert result[0]["is_active"] == True #noqa: E712
    assert result[1]["is_active"] == False #noqa: E712