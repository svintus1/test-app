from sqlmodel import SQLModel, create_engine, delete, Session 
import os
from app.models import Test
from app.core.config import POSTGRES_HOST, POSTGRES_PORT

print(POSTGRES_PORT)
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{POSTGRES_HOST}:{POSTGRES_PORT}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)
    # Создаём сессию вручную
    with Session(engine) as session:
        # Проверяем, есть ли уже данные в таблице (чтобы избежать дублирования)
        statement = delete(Test)
        session.exec(statement)

        hello = Test(hello="Привет, ")
        session.add(hello)
        session.commit()
        print("Добавлена тестовая запись:", hello.hello)
    

def get_session():
    with Session(engine) as session:
        yield session
