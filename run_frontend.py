#!/usr/bin/env python3
"""
Script to run the LinkedIn Personal Branding AI Agent frontend application
"""

import subprocess
import sys
import os

def run_frontend():
    """
    Run the React frontend application
    """
    print("Starting LinkedIn Personal Branding AI Agent frontend...")
    
    # Change to the frontend directory
    frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
    
    if not os.path.exists(frontend_path):
        print("Error: frontend directory not found.")
        return False
    
    try:
        # Change to the frontend directory
        os.chdir(frontend_path)
        
        # Check if node_modules exists, if not install dependencies
        if not os.path.exists("node_modules"):
            print("Installing frontend dependencies...")
            subprocess.run(["npm", "install"], check=True)
        
        # Run the React development server
        print("Starting React development server...")
        result = subprocess.run(["npm", "start"], check=True)
        
        print("\nFrontend application stopped.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nFrontend application failed with return code {e.returncode}")
        return False
    except KeyboardInterrupt:
        print("\nFrontend application stopped by user.")
        return True
    except FileNotFoundError:
        print("Error: npm not found. Please install Node.js and npm.")
        return False

if __name__ == "__main__":
    success = run_frontend()
    sys.exit(0 if success else 1)