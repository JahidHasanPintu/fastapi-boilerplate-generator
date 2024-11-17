import os

# Prompt user for project name
project_name = input("Enter your project name: ")

if not project_name.strip():
    print("Project name cannot be empty!")
    exit(1)

# Directory structure
structure = {
    "app": [
        "config", "api/v1/routes", "api/v1/endpoints", "core",
        "models", "schemas", "services", "repositories", "utils", "middlewares", "tasks", "workers", "static"
    ],
    "tests": ["api", "services", "repositories"],
    "migrations": [],
}

# Files to create
files = {
    f"{project_name}/.gitignore": "__pycache__/\n.env\n*.pyc",
    f"{project_name}/README.md": f"# {project_name}\nAn enterprise-level FastAPI boilerplate project.",
    f"{project_name}/requirements.txt": "fastapi\nuvicorn\npydantic\nsqlalchemy\nhttpx\nalembic\npytest",
    f"{project_name}/app/main.py": """from fastapi import FastAPI
from app.api.v1.routes import user, project
app = FastAPI(title="FastAPI Enterprise Application")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}""",
    f"{project_name}/app/config/settings.py": """from pydantic import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
settings = Settings()""",
    f"{project_name}/tests/test_main.py": """from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}""",
}

# Create directories
def create_directories():
    for folder, subfolders in structure.items():
        for sub in subfolders:
            os.makedirs(os.path.join(project_name, folder, sub), exist_ok=True)

# Create files
def create_files():
    for file_path, content in files.items():
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)

# Main execution
if __name__ == "__main__":
    os.makedirs(project_name, exist_ok=True)
    create_directories()
    create_files()
    print(f"FastAPI project structure created successfully for {project_name}!")
