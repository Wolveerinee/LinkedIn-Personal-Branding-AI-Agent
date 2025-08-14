#!/usr/bin/env python3
"""
Script to run the LinkedIn Personal Branding AI Agent using Docker Compose
"""

import subprocess
import sys
import os

def run_docker():
    """
    Run the application using Docker Compose
    """
    print("Starting LinkedIn Personal Branding AI Agent with Docker Compose...")
    
    try:
        # Check if docker-compose.yml exists
        if not os.path.exists("docker-compose.yml"):
            print("Error: docker-compose.yml not found.")
            return False
        
        # Run docker-compose up
        print("Building and starting containers...")
        result = subprocess.run(["docker-compose", "up", "--build"], check=True)
        
        print("\nApplication stopped.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nDocker Compose failed with return code {e.returncode}")
        return False
    except KeyboardInterrupt:
        print("\nStopping containers...")
        subprocess.run(["docker-compose", "down"])
        print("Application stopped.")
        return True
    except FileNotFoundError:
        print("Error: docker-compose not found. Please install Docker and Docker Compose.")
        return False

def stop_docker():
    """
    Stop the application using Docker Compose
    """
    print("Stopping LinkedIn Personal Branding AI Agent containers...")
    
    try:
        # Run docker-compose down
        result = subprocess.run(["docker-compose", "down"], check=True)
        
        print("Containers stopped successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nDocker Compose failed with return code {e.returncode}")
        return False
    except FileNotFoundError:
        print("Error: docker-compose not found. Please install Docker and Docker Compose.")
        return False

def show_logs():
    """
    Show logs from Docker Compose
    """
    print("Showing application logs...")
    
    try:
        # Run docker-compose logs
        result = subprocess.run(["docker-compose", "logs", "-f"], check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nDocker Compose logs failed with return code {e.returncode}")
        return False
    except FileNotFoundError:
        print("Error: docker-compose not found. Please install Docker and Docker Compose.")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "stop":
            success = stop_docker()
        elif command == "logs":
            success = show_logs()
        else:
            print(f"Unknown command: {command}")
            print("Usage: python run_docker.py [stop|logs]")
            sys.exit(1)
    else:
        success = run_docker()
    
    sys.exit(0 if success else 1)