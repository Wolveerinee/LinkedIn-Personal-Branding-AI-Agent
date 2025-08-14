from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    linkedin_profile_url = Column(String, unique=True, index=True)
    name = Column(String)
    headline = Column(String)
    about = Column(Text)
    skills = Column(Text)  # JSON string of skills
    experience = Column(Text)  # JSON string of experience
    education = Column(Text)  # JSON string of education
    interests = Column(Text)  # JSON string of interests
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())