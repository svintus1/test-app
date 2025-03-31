import os
from dotenv import load_dotenv

# Считываем переменную окружения APP_ENV
env = os.getenv("APP_ENV")  # по умолчанию development
if env not in ("development", "production", "staging"):
    env = "development"

# Загружем переменные окружения из .env-файла в зависимости от значения APP_ENV
load_dotenv(f"./.env.{env}", override=True)

BACKEND_HOST = os.getenv("BACKEND_HOST")
BACKEND_PORT = int(os.getenv("BACKEND_PORT"))
FRONTEND_HOST = os.getenv("FRONTEND_HOST")
FRONTEND_PORT = int(os.getenv("FRONTEND_PORT"))
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT"))