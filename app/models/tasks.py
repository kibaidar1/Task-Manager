from datetime import datetime

from sqlalchemy import Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Task(Base):
    title: Mapped[str]
    description: Mapped[str]
    due_date: Mapped[datetime.date] = mapped_column(Date)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship("User",
                                        back_populates="tasks")
