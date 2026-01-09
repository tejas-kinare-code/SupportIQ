"""
Application configuration settings.
"""
import os
from pathlib import Path
from typing import List


# Base directory
BASE_DIR = Path(__file__).parent.parent

# Data directory
DATA_DIR = BASE_DIR / "data"

# Department folders
DEPARTMENTS = ["hr", "it", "policy"]

# Document processing settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# CORS settings
CORS_ORIGINS: List[str] = [
    "http://localhost:3000",
    "http://localhost:5173",
]

# API settings
API_PREFIX = "/api"


