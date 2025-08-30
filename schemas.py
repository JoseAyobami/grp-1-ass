from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional


class UserBase(BaseModel):
    username: str = Field(min_length=5, max_length=20)
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: UUID


class Post(BaseModel):
    id: UUID
    username: str
    title: str
    content: str
    image_filename: Optional[str] = None
    likes: int = 0

    
    

    
