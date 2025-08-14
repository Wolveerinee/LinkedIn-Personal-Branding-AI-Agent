#!/usr/bin/env python3
"""
Script to run the LinkedIn Personal Branding AI Agent backend application
"""

import subprocess
import sys
import os

def run_backend():
    """
    Run the FastAPI backend application
    """
    print("Starting LinkedIn Personal Branding AI Agent backend...")
    
    # Run the FastAPI application
    try:
        # Change to the backend directory
        backend_path = os.path.join(os.path.dirname(__file__), "backend")
        os.chdir(backend_path)
        
        # Run uvicorn server
        result = subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload"
        ], check=True)
        
        print("\nBackend application stopped.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nBackend application failed with return code {e.returncode}")
        return False
    except KeyboardInterrupt:
        print("\nBackend application stopped by user.")
        return True
    except FileNotFoundError:
        print("Error: uvicorn not found. Please install it with 'pip install uvicorn'")
        return False

if __name__ == "__main__":
    success = run_backend()
    sys.exit(0 if success else 1)