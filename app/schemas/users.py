from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    username: str
    email: EmailStr


class UserRead(UserCreate):
    id: int

    model_config = ConfigDict(from_attributes=True,
                              arbitrary_types_allowed=True)
