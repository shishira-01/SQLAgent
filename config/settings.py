from pydantic_settings import BaseSettings, SettingsConfigDict
import os 
from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

# Determine the environment
ENV = os.environ.get("ENV", "development")

# Set up the path for the .env file
if ENV == "development":
    # In development, look for .env file in the project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    env_path = os.path.join(project_root, '.env')
    
    # Load environment variables from .env file
    load_dotenv(dotenv_path=env_path)
    print(f"Development: Loading .env file from: {env_path}")
else:
    # In production, we'll use environment variables directly
    env_path = None
    print("Production: Using environment variables")

class AppSettings(BaseSettings):
    GEMINI_API_KEY: str
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT_NUMBER: str
    
    model_config = SettingsConfigDict(
        env_file=env_path if ENV == "development" else None,
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Initialize settings
Appsettings = AppSettings()

# Debug: Print loaded values (consider removing in production)
print(f"GEMINI_API_KEY loaded: {'Yes' if Appsettings.GEMINI_API_KEY else 'No'}")
print(f"DB_HOST loaded: {'Yes' if Appsettings.DB_HOST else 'No'}")

