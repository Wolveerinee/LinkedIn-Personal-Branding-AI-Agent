from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import os

from .. import schemas, models, database
from ..services import linkedin_service

router = APIRouter()

@router.post("/authenticate")
def authenticate_linkedin(profile_url: str, db: Session = Depends(database.get_db)):
    """
    Authenticate with LinkedIn API using OAuth 2.0
    """
    try:
        # In a real implementation, this would redirect to LinkedIn's OAuth flow
        # For now, we'll simulate the process
        access_token = linkedin_service.get_access_token(profile_url)
        return {"access_token": access_token, "status": "authenticated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profile/{user_id}")
def get_linkedin_profile(user_id: int, db: Session = Depends(database.get_db)):
    """
    Get user's LinkedIn profile information
    """
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        profile_data = linkedin_service.get_user_profile(user.linkedin_profile_url)
        return profile_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/post/{content_id}")
def post_to_linkedin(content_id: int, db: Session = Depends(database.get_db)):
    """
    Post content to LinkedIn
    """
    try:
        content = db.query(models.Content).filter(models.Content.id == content_id).first()
        if content is None:
            raise HTTPException(status_code=404, detail="Content not found")
        
        post_result = linkedin_service.post_content(content)
        # Update content with LinkedIn post ID
        content.linkedin_post_id = post_result.get("post_id")
        content.posted = True
        db.commit()
        db.refresh(content)
        
        return {"message": "Content posted successfully", "post_id": post_result.get("post_id")}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/analytics/{content_id}")
def get_linkedin_analytics(content_id: int, db: Session = Depends(database.get_db)):
    """
    Get analytics for a LinkedIn post
    """
    try:
        content = db.query(models.Content).filter(models.Content.id == content_id).first()
        if content is None:
            raise HTTPException(status_code=404, detail="Content not found")
        
        if not content.linkedin_post_id:
            raise HTTPException(status_code=400, detail="Content not posted to LinkedIn yet")
        
        analytics_data = linkedin_service.get_post_analytics(content.linkedin_post_id)
        return analytics_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))