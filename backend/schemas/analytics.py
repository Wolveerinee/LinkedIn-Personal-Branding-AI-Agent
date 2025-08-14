from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AnalyticsBase(BaseModel):
    content_id: int
    likes: Optional[int] = 0
    comments: Optional[int] = 0
    shares: Optional[int] = 0
    impressions: Optional[int] = 0
    engagement_rate: Optional[int] = 0
    reach: Optional[int] = 0

class AnalyticsCreate(AnalyticsBase):
    pass

class AnalyticsUpdate(AnalyticsBase):
    pass

class Analytics(AnalyticsBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True