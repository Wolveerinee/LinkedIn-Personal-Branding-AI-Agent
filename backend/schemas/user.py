from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    linkedin_profile_url: str
    name: Optional[str] = None
    headline: Optional[str] = None
    about: Optional[str] = None
    skills: Optional[str] = None
    experience: Optional[str] = None
    education: Optional[str] = None
    interests: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True