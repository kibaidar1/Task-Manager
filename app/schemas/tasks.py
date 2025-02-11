from datetime import date, UTC, datetime

from pydantic import BaseModel, Field, ConfigDict


class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: date
    user_id: int


class TaskRead(TaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True,
                              arbitrary_types_allowed=True)


class TaskUpdate(TaskCreate):
    title: str = ''
    description: str = 'None'
    due_date: date = None
    user_id: int = 0

