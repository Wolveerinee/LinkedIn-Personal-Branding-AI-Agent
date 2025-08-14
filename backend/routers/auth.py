from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional
import hashlib
import os

from .. import schemas, models, database
from ..services import linkedin_service

router = APIRouter()

# OAuth2 scheme for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Secret key for JWT tokens (in production, use environment variables)
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token
    """
    from jose import jwt
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    """
    Get the current user from the JWT token
    """
    from jose import JWTError, jwt
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    return user

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), 
                                 db: Session = Depends(database.get_db)):
    """
    Login endpoint to get an access token
    In a real implementation, you would verify username/password
    For this example, we'll simulate LinkedIn OAuth
    """
    # In a real implementation, you would:
    # 1. Verify the user's credentials
    # 2. Check if the user exists in the database
    # 3. Create and return an access token
    
    # For now, we'll simulate the process
    user = db.query(models.User).filter(models.User.linkedin_profile_url == form_data.username).first()
    
    if not user:
        # Create a new user if they don't exist
        user_data = {
            "linkedin_profile_url": form_data.username,
            "name": "LinkedIn User",
            "headline": "LinkedIn Professional"
        }
        user = models.User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/linkedin")
async def linkedin_auth(request: Request, db: Session = Depends(database.get_db)):
    """
    Authenticate with LinkedIn OAuth
    """
    # In a real implementation, this would redirect to LinkedIn's OAuth flow
    # For now, we'll simulate the process
    
    # Get the LinkedIn profile URL from the request
    profile_url = request.query_params.get("profile_url")
    
    if not profile_url:
        raise HTTPException(status_code=400, detail="Profile URL is required")
    
    # Check if user exists, create if not
    user = db.query(models.User).filter(models.User.linkedin_profile_url == profile_url).first()
    
    if not user:
        # Get user profile from LinkedIn
        try:
            profile_data = linkedin_service.get_user_profile(profile_url)
            user_data = {
                "linkedin_profile_url": profile_url,
                "name": profile_data.get("name", ""),
                "headline": profile_data.get("headline", ""),
                "about": profile_data.get("about", ""),
                "skills": str(profile_data.get("skills", [])),
                "experience": str(profile_data.get("experience", [])),
                "education": str(profile_data.get("education", [])),
                "interests": str(profile_data.get("interests", []))
            }
            user = models.User(**user_data)
            db.add(user)
            db.commit()
            db.refresh(user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to fetch LinkedIn profile: {str(e)}")
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "user_id": user.id
    }

@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    """
    Get the current user's profile
    """
    return current_user

@router.post("/logout")
async def logout(current_user: models.User = Depends(get_current_user)):
    """
    Logout the current user
    In a real implementation, you would invalidate the token
    """
    # In a real implementation, you would:
    # 1. Add the token to a blacklist
    # 2. Set an expiration time for the token
    # 3. Return a success message
    
    return {"message": "Successfully logged out"}