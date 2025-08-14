from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ContentBase(BaseModel):
    user_id: int
    title: Optional[str] = None
    body: str
    content_type: str
    hashtags: Optional[str] = None
    scheduled_time: Optional[datetime] = None
    posted: Optional[bool] = False
    linkedin_post_id: Optional[str] = None
    engagement_score: Optional[int] = 0

class ContentCreate(ContentBase):
    pass

class ContentUpdate(ContentBase):
    pass

class Content(ContentBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True