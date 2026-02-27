from typing import Optional

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    owner_id: Optional[int] = None


class ItemRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner_id: Optional[int] = None


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None


class UserRead(BaseModel):
    id: int
    username: str
    full_name: Optional[str] = None
