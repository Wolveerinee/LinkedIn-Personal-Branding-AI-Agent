import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app
from ..database import Base, get_db
from ..models import user, content, analytics

# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# Override get_db dependency
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "LinkedIn Personal Branding AI Agent API"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_user():
    user_data = {
        "linkedin_profile_url": "https://www.linkedin.com/in/testuser",
        "name": "Test User",
        "headline": "Software Engineer",
        "about": "Test user for API testing",
        "skills": "[\"Python\", \"JavaScript\"]",
        "experience": "[{\"title\": \"Developer\", \"company\": \"Test Corp\"}]",
        "education": "[{\"degree\": \"BSc Computer Science\", \"institution\": \"Test University\"}]",
        "interests": "[\"Technology\", \"AI\"]"
    }
    
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert "id" in data

def test_get_user():
    # First create a user
    user_data = {
        "linkedin_profile_url": "https://www.linkedin.com/in/testuser2",
        "name": "Test User 2",
        "headline": "Data Scientist",
        "about": "Another test user",
        "skills": "[\"Python\", \"Machine Learning\"]",
        "experience": "[{\"title\": \"Data Scientist\", \"company\": \"Test AI Corp\"}]",
        "education": "[{\"degree\": \"MSc Data Science\", \"institution\": \"Test AI University\"}]",
        "interests": "[\"AI\", \"Machine Learning\"]"
    }
    
    create_response = client.post("/api/v1/users/", json=user_data)
    assert create_response.status_code == 201
    created_user = create_response.json()
    user_id = created_user["id"]
    
    # Then get the user
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User 2"
    assert data["id"] == user_id

def test_create_content():
    # First create a user to associate content with
    user_data = {
        "linkedin_profile_url": "https://www.linkedin.com/in/testuser3",
        "name": "Test User 3",
        "headline": "Content Creator",
        "about": "Test user for content creation",
        "skills": "[\"Writing\", \"Content Strategy\"]",
        "experience": "[{\"title\": \"Content Specialist\", \"company\": \"Test Content Corp\"}]",
        "education": "[{\"degree\": \"BA Communications\", \"institution\": \"Test Communications University\"}]",
        "interests": "[\"Content Marketing\", \"Social Media\"]"
    }
    
    create_user_response = client.post("/api/v1/users/", json=user_data)
    assert create_user_response.status_code == 201
    created_user = create_user_response.json()
    user_id = created_user["id"]
    
    # Then create content
    content_data = {
        "user_id": user_id,
        "title": "Test Content",
        "body": "This is a test content post",
        "content_type": "text",
        "hashtags": "[\"#test\", \"#content\"]",
        "scheduled_time": "2025-08-15T08:00:00Z"
    }
    
    response = client.post("/api/v1/content/", json=content_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Content"
    assert "id" in data

def test_get_content():
    # First create a user and content
    user_data = {
        "linkedin_profile_url": "https://www.linkedin.com/in/testuser4",
        "name": "Test User 4",
        "headline": "Content Manager",
        "about": "Test user for content retrieval",
        "skills": "[\"Content Management\", \"Strategy\"]",
        "experience": "[{\"title\": \"Content Manager\", \"company\": \"Test Management Corp\"}]",
        "education": "[{\"degree\": \"MA Digital Media\", \"institution\": \"Test Media University\"}]",
        "interests": "[\"Digital Media\", \"Content Strategy\"]"
    }
    
    create_user_response = client.post("/api/v1/users/", json=user_data)
    assert create_user_response.status_code == 201
    created_user = create_user_response.json()
    user_id = created_user["id"]
    
    # Create content
    content_data = {
        "user_id": user_id,
        "title": "Test Content 2",
        "body": "This is another test content post",
        "content_type": "article",
        "hashtags": "[\"#test2\", \"#article\"]",
        "scheduled_time": "2025-08-16T12:00:00Z"
    }
    
    create_content_response = client.post("/api/v1/content/", json=content_data)
    assert create_content_response.status_code == 201
    created_content = create_content_response.json()
    content_id = created_content["id"]
    
    # Then get the content
    response = client.get(f"/api/v1/content/{content_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Content 2"
    assert data["id"] == content_id

def test_get_user_content():
    # First create a user
    user_data = {
        "linkedin_profile_url": "https://www.linkedin.com/in/testuser5",
        "name": "Test User 5",
        "headline": "Content Analyst",
        "about": "Test user for content analysis",
        "skills": "[\"Analysis\", \"Content Strategy\"]",
        "experience": "[{\"title\": \"Content Analyst\", \"company\": \"Test Analysis Corp\"}]",
        "education": "[{\"degree\": \"MS Analytics\", \"institution\": \"Test Analytics University\"}]",
        "interests": "[\"Content Analytics\", \"Data Analysis\"]"
    }
    
    create_user_response = client.post("/api/v1/users/", json=user_data)
    assert create_user_response.status_code == 201
    created_user = create_user_response.json()
    user_id = created_user["id"]
    
    # Create content for the user
    content_data = {
        "user_id": user_id,
        "title": "Test Content 3",
        "body": "This is a third test content post",
        "content_type": "carousel",
        "hashtags": "[\"#test3\", \"#carousel\"]",
        "scheduled_time": "2025-08-17T15:00:00Z"
    }
    
    create_content_response = client.post("/api/v1/content/", json=content_data)
    assert create_content_response.status_code == 201
    
    # Then get user's content
    response = client.get(f"/api/v1/content/user/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["title"] == "Test Content 3"
    assert data[0]["user_id"] == user_id