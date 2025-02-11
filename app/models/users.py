from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.database import Base


class User(Base):
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str]
    tasks: Mapped[List["Task"]] = relationship("Task",
                                               back_populates='user',
                                               uselist=True,
                                               cascade='all, delete-orphan')
