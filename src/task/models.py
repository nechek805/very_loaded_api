from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[String] = mapped_column(String(255))
    start: Mapped[DateTime] = mapped_column()
    end: Mapped[DateTime] = mapped_column()
    is_active: Mapped[Boolean] = mapped_column(default=True)