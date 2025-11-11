
"""
Configuration module.
Loads environment variables and provides global application settings.
"""


import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
