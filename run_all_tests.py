#!/usr/bin/env python3
"""
Script to run all tests for the LinkedIn Personal Branding AI Agent
"""

import subprocess
import sys
import os

def run_all_tests():
    """
    Run all tests for the application
    """
    print("Running all tests for LinkedIn Personal Branding AI Agent...")
    
    # Run pytest for all tests
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "backend/tests/", 
            "-v", 
            "--cov=backend",
            "--cov-report=html:htmlcov",
            "--cov-report=term-missing"
        ], check=True)
        
        print("\nAll tests completed successfully!")
        print("Coverage report available in htmlcov/index.html")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nTests failed with return code {e.returncode}")
        return False
    except FileNotFoundError:
        print("Error: pytest not found. Please install it with 'pip install pytest'")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)