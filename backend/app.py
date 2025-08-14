import uvicorn
import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables
load_dotenv()

def main():
    # Import the FastAPI app
    from backend.main import app
    
    # Get host and port from environment variables or use defaults
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    reload = os.getenv("DEBUG", "True").lower() == "true"
    
    # Run the FastAPI application
    uvicorn.run(
        "backend.main:app",
        host=host,
        port=port,
        reload=reload
    )

if __name__ == "__main__":
    main()