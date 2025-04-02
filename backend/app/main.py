from fastapi import FastAPI
from app.core.database import init_db
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.core.config import BACKEND_HOST, BACKEND_PORT, FRONTEND_HOST, FRONTEND_PORT
from app.api.main import api_router
import os

app = FastAPI()

# Разрешите запросы с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://{FRONTEND_HOST}:{FRONTEND_PORT}"],  # Укажите адрес вашего фронтенда
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(api_router)

# Инициализация БД
init_db()


if __name__ == "__main__":
    is_dev = os.getenv("APP_ENV", "development") == "development"
    uvicorn.run("main:app", host=BACKEND_HOST, port=BACKEND_PORT, reload=is_dev)