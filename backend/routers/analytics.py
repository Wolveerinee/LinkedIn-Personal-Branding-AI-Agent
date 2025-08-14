from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models, database

router = APIRouter()

@router.post("/", response_model=schemas.Analytics, status_code=status.HTTP_201_CREATED)
def create_analytics(analytics: schemas.AnalyticsCreate, db: Session = Depends(database.get_db)):
    db_analytics = models.Analytics(**analytics.dict())
    db.add(db_analytics)
    db.commit()
    db.refresh(db_analytics)
    return db_analytics

@router.get("/{analytics_id}", response_model=schemas.Analytics)
def get_analytics(analytics_id: int, db: Session = Depends(database.get_db)):
    db_analytics = db.query(models.Analytics).filter(models.Analytics.id == analytics_id).first()
    if db_analytics is None:
        raise HTTPException(status_code=404, detail="Analytics not found")
    return db_analytics

@router.put("/{analytics_id}", response_model=schemas.Analytics)
def update_analytics(analytics_id: int, analytics: schemas.AnalyticsUpdate, db: Session = Depends(database.get_db)):
    db_analytics = db.query(models.Analytics).filter(models.Analytics.id == analytics_id).first()
    if db_analytics is None:
        raise HTTPException(status_code=404, detail="Analytics not found")
    
    for key, value in analytics.dict().items():
        setattr(db_analytics, key, value)
    
    db.commit()
    db.refresh(db_analytics)
    return db_analytics

@router.get("/", response_model=List[schemas.Analytics])
def get_analytics_list(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    analytics = db.query(models.Analytics).offset(skip).limit(limit).all()
    return analytics

@router.get("/content/{content_id}", response_model=schemas.Analytics)
def get_content_analytics(content_id: int, db: Session = Depends(database.get_db)):
    analytics = db.query(models.Analytics).filter(models.Analytics.content_id == content_id).first()
    if analytics is None:
        raise HTTPException(status_code=404, detail="Analytics not found for this content")
    return analytics