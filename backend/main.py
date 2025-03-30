from fastapi import FastAPI, Query, Depends
from models import Test
from database import init_db, get_session, Session
from sqlmodel import select
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешите запросы с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://188.243.140.226:3000"],  # Укажите адрес вашего фронтенда
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Инициализация БД
init_db()

# HTTP-эндпоинты
@app.get("/")
async def get_homepage(name: Annotated[str | None, Query()] = "test", session: Session = Depends(get_session)):
    test_data = session.exec(select(Test)).first()
    return {"message": f"{test_data.hello}{name}"}