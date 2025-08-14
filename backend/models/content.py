from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.sql import func
from ..database import Base

class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    body = Column(Text)
    content_type = Column(String)  # text, carousel, article, poll
    hashtags = Column(Text)  # JSON string of hashtags
    scheduled_time = Column(DateTime(timezone=True))
    posted = Column(Boolean, default=False)
    linkedin_post_id = Column(String, nullable=True)
    engagement_score = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())