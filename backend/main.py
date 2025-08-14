from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, content, analytics, linkedin, auth
from .database import engine, Base

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LinkedIn Personal Branding AI Agent",
    description="An autonomous AI agent that researches, creates, and posts LinkedIn content for personal branding.",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(content.router, prefix="/api/v1/content", tags=["content"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])
app.include_router(linkedin.router, prefix="/api/v1/linkedin", tags=["linkedin"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "LinkedIn Personal Branding AI Agent API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}