#!/usr/bin/env python3
"""
Script to deploy the LinkedIn Personal Branding AI Agent application
"""

import subprocess
import sys
import os
import argparse

def build_images():
    """
    Build Docker images for the application
    """
    print("Building Docker images...")
    
    try:
        # Build the images
        result = subprocess.run(["docker-compose", "build"], check=True)
        print("Docker images built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to build Docker images with return code {e.returncode}")
        return False
    except FileNotFoundError:
        print("Error: docker-compose not found. Please install Docker and Docker Compose.")
        return False

def start_application():
    """
    Start the application using Docker Compose
    """
    print("Starting application with Docker Compose...")
    
    try:
        # Start the application
        result = subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("Application started successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to start application with return code {e.returncode}")
        return False
    except FileNotFoundError:
        print("Error: docker-compose not found. Please install Docker and Docker Compose.")
        return False

def stop_application():
    """
    Stop the application using Docker Compose
    """
    print("Stopping application...")
    
    try:
        # Stop the application
        result = subprocess.run(["docker-compose", "down"], check=True)
        print("Application stopped successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop application with return code {e.returncode}")
        return False
    except FileNotFoundError:
        print("Error: docker-compose not found. Please install Docker and Docker Compose.")
        return False

def show_logs():
    """
    Show application logs
    """
    print("Showing application logs...")
    
    try:
        # Show logs
        result = subprocess.run(["docker-compose", "logs", "-f"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to show logs with return code {e.returncode}")
        return False
    except FileNotFoundError:
        print("Error: docker-compose not found. Please install Docker and Docker Compose.")
        return False

def deploy_application():
    """
    Deploy the application by building images and starting services
    """
    print("Deploying LinkedIn Personal Branding AI Agent application...")
    
    # Build images
    if not build_images():
        return False
    
    # Start application
    if not start_application():
        return False
    
    print("\nApplication deployed successfully!")
    print("Backend API available at: http://localhost:8000")
    print("Frontend available at: http://localhost:3000")
    return True

def main():
    parser = argparse.ArgumentParser(description="Deploy LinkedIn Personal Branding AI Agent")
    parser.add_argument("action", choices=["deploy", "start", "stop", "logs", "build"], 
                        help="Action to perform")
    
    args = parser.parse_args()
    
    if args.action == "deploy":
        success = deploy_application()
    elif args.action == "start":
        success = start_application()
    elif args.action == "stop":
        success = stop_application()
    elif args.action == "logs":
        success = show_logs()
    elif args.action == "build":
        success = build_images()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()