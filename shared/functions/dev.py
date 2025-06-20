import os

def isDevelopment() -> bool:
    return os.getenv("ENVIRONMENT", "development") == "development"