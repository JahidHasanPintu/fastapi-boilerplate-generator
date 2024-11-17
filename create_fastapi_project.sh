#!/bin/bash

# Prompt user for project name
read -p "Enter your project name: " PROJECT_NAME

if [ -z "$PROJECT_NAME" ]; then
    echo "Project name cannot be empty!"
    exit 1
fi

# Create root directory
mkdir $PROJECT_NAME && cd $PROJECT_NAME

# Create root files
touch .env .gitignore README.md requirements.txt Dockerfile docker-compose.yml pyproject.toml

# Create main directories
mkdir app tests migrations

# Create app subdirectories
mkdir -p app/{config,api/core,models,schemas,services,repositories,utils,middlewares,tasks,workers,static}

# Create API versioning directories
mkdir -p app/api/v1/{routes,endpoints}

# Root example files
cat <<EOF > .gitignore
__pycache__/
.env
*.pyc
EOF

cat <<EOF > README.md
# $PROJECT_NAME
An enterprise-level FastAPI boilerplate project.
EOF

cat <<EOF > requirements.txt
fastapi
uvicorn
pydantic
sqlalchemy
httpx
alembic
pytest
EOF

# Create app/main.py
cat <<EOF > app/main.py
from fastapi import FastAPI
from app.api.v1.routes import user, project
from app.config.settings import settings

app = FastAPI(title="Enterprise FastAPI Application", version="1.0.0")

# Include API routes
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(project.router, prefix="/api/v1/projects", tags=["Projects"])

# Health Check
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}
EOF

cat <<EOF > app/config/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    API_VERSION: str = "/api/v1"
    
    class Config:
        env_file = ".env"

settings = Settings()
EOF

cat <<EOF > tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
EOF

echo "Boilerplate structure created successfully for $PROJECT_NAME!"
