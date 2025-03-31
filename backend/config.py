import os
from dotenv import load_dotenv

# Считываем переменную окружения APP_ENV
env = os.getenv("APP_ENV", "development")  # по умолчанию development
if env not in ("development", "production"):
    env = "development"
# Загружем переменные окружения из .env.development или .env.production в зависимости от значения APP_ENV
load_dotenv(f".env.production")

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))