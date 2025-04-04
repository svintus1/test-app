import os

# Считываем переменную окружения APP_ENV
APP_ENV = os.getenv("APP_ENV")  # по умолчанию development
if APP_ENV not in ("development", "production", "staging"):
    APP_ENV = "development"

BACKEND_HOST = os.getenv("BACKEND_HOST")
BACKEND_PORT = int(os.getenv("BACKEND_PORT"))
FRONTEND_HOST = os.getenv("FRONTEND_HOST")
FRONTEND_PORT = int(os.getenv("FRONTEND_PORT"))
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT"))