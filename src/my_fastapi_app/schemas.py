from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str
    age: int

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True