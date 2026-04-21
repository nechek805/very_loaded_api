from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from src.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    start: Mapped[datetime] = mapped_column()
    end: Mapped[datetime] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)