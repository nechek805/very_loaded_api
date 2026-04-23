from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title: str
    start: datetime
    end: datetime
    is_active: bool = True


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    start: datetime
    end: datetime

class TaskUpdate(BaseModel):
    title: str | None = None
    start: datetime | None = None
    end: datetime | None = None