from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models, database

router = APIRouter()

@router.post("/", response_model=schemas.Content, status_code=status.HTTP_201_CREATED)
def create_content(content: schemas.ContentCreate, db: Session = Depends(database.get_db)):
    db_content = models.Content(**content.dict())
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

@router.get("/{content_id}", response_model=schemas.Content)
def get_content(content_id: int, db: Session = Depends(database.get_db)):
    db_content = db.query(models.Content).filter(models.Content.id == content_id).first()
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content

@router.put("/{content_id}", response_model=schemas.Content)
def update_content(content_id: int, content: schemas.ContentUpdate, db: Session = Depends(database.get_db)):
    db_content = db.query(models.Content).filter(models.Content.id == content_id).first()
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    
    for key, value in content.dict().items():
        setattr(db_content, key, value)
    
    db.commit()
    db.refresh(db_content)
    return db_content

@router.get("/", response_model=List[schemas.Content])
def get_contents(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    contents = db.query(models.Content).offset(skip).limit(limit).all()
    return contents

@router.get("/user/{user_id}", response_model=List[schemas.Content])
def get_user_contents(user_id: int, db: Session = Depends(database.get_db)):
    contents = db.query(models.Content).filter(models.Content.user_id == user_id).all()
    return contents