from sqlmodel import SQLModel, create_engine, select, Session 
import os
from models import Test
from config import POSTGRES_HOST, POSTGRES_PORT

print(POSTGRES_PORT)
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{POSTGRES_HOST}:{POSTGRES_PORT}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)
    # Создаём сессию вручную
    with Session(engine) as session:
        # Проверяем, есть ли уже данные в таблице (чтобы избежать дублирования)
        statement = select(Test)
        tests = session.exec(statement).all()
        for test in tests:
            session.delete(test)

        hello = Test(hello="Надо было поменять для теста, я и поменял - ")
        session.add(hello)
        session.commit()
        print("Добавлена тестовая запись:", hello)
    

def get_session():
    with Session(engine) as session:
        yield session
