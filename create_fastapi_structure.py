import os
import sys


def create_file(file_path, content=""):
    """Create a file with the given content."""
    with open(file_path, "w") as file:
        file.write(content)


def create_folder_structure(project_name):
    """Create the folder structure for the FastAPI project."""
    # Root directory
    os.makedirs(project_name, exist_ok=True)

    # App structure
    app_dirs = [
        "app/api/v1/endpoints",
        "app/api/v1/routes",
        "app/config",
        "app/core",
        "app/middlewares",
        "app/models",
        "app/repositories",
        "app/schemas",
        "app/services",
        "app/static",
        "app/tasks",
        "app/utils",
        "app/workers"
    ]
    for directory in app_dirs:
        os.makedirs(os.path.join(project_name, directory), exist_ok=True)

    # Migrations and tests
    os.makedirs(os.path.join(project_name, "migrations"), exist_ok=True)
    test_dirs = [
        "tests/api",
        "tests/repositories",
        "tests/services"
    ]
    for directory in test_dirs:
        os.makedirs(os.path.join(project_name, directory), exist_ok=True)

    # Create example files
    create_file(
        os.path.join(project_name, "app/main.py"),
        content="""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}
""",
    )

    create_file(
        os.path.join(project_name, "app/config/settings.py"),
        content="""from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Application"
    debug: bool = True

settings = Settings()
""",
    )

    create_file(
        os.path.join(project_name, "tests/test_main.py"),
        content="""from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}
""",
    )

    # Create other project-level files
    create_file(
        os.path.join(project_name, ".gitignore"),
        content=""".env
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
env.bak/
venv.bak/
.idea/
.vscode/
migrations/
*.sqlite3
""",
    )

    create_file(
        os.path.join(project_name, "requirements.txt"),
        content="""fastapi
uvicorn[standard]
pydantic
httpx
pytest
""",
    )

    create_file(
        os.path.join(project_name, "Dockerfile"),
        content="""# Dockerfile for FastAPI
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
""",
    )

    create_file(
        os.path.join(project_name, "docker-compose.yml"),
        content="""version: "3.8"

services:
  fastapi_app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - ENV=dev
""",
    )

    create_file(
        os.path.join(project_name, "pyproject.toml"),
        content="""[tool.poetry]
name = "fastapi-app"
version = "0.1.0"
description = "A FastAPI project"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
""",
    )

    create_file(
        os.path.join(project_name, ".env"),
        content="""DEBUG=True
APP_NAME=FastAPI Application
""",
    )

    create_file(
        os.path.join(project_name, "README.md"),
        content=f"""# {project_name}

This is a boilerplate FastAPI project with an enterprise-level folder structure.

## **How to Run**

1. Install dependencies:
"""
    )


if __name__ == "__main__":
    print("Welcome to the FastAPI Boilerplate Generator!")

    # Get the project name from the user
    project_name = input("Enter your project name: ").strip()

    if not project_name:
        print("Error: Project name cannot be empty.")
        sys.exit(1)

    # Create the folder structure
    create_folder_structure(project_name)

    print(f"FastAPI boilerplate for '{project_name}' has been created successfully!")
    print(f"Navigate to the '{project_name}' directory to get started.")
