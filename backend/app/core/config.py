import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Configuration settings for the application."""
    
    # Recall API configuration
    RECALL_API_KEY = os.getenv("RECALL_API_KEY")
    RECALL_REGION = os.getenv("RECALL_REGION", "us-west-2")
    RECALL_WEBHOOK_URL = os.getenv("RECALL_WEBHOOK_URL")
    
    # OpenAI configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Session mode: 'production' for real calls, 'simulation' for testing
    SESSION_MODE = os.getenv("SESSION_MODE", "production")
    
    # CORS configuration
    CORS_ORIGINS = ["http://localhost:3000", "http://localhost:5173", "*"]
    
    # Indicator observability configuration
    INDICATOR_OBSERVABILITY_ENABLED = os.getenv("INDICATOR_OBSERVABILITY_ENABLED", "false").lower() == "true"
    INDICATOR_LOG_PATH = os.getenv("INDICATOR_LOG_PATH", "observability_logs")
    
    # Application base URL for webhooks and media streaming
    APP_BASE_URL = os.getenv("APP_BASE_URL", "http://localhost:8000")


# Create settings instance
settings = Settings()

# For backward compatibility, expose individual variables
RECALL_API_KEY = settings.RECALL_API_KEY
RECALL_REGION = settings.RECALL_REGION
RECALL_WEBHOOK_URL = settings.RECALL_WEBHOOK_URL
OPENAI_API_KEY = settings.OPENAI_API_KEY
SESSION_MODE = settings.SESSION_MODE
CORS_ORIGINS = settings.CORS_ORIGINS