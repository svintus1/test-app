from sqlmodel import SQLModel, create_engine, select, Session
from dotenv import load_dotenv
import os
from models import Test

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)
    # Создаём сессию вручную
    with Session(engine) as session:
        # Проверяем, есть ли уже данные в таблице (чтобы избежать дублирования)
        if not session.exec(select(Test)).first():
            hello = Test(hello="Hello world! My name is ")
            session.add(hello)
            session.commit()
            print("Добавлена тестовая запись:", hello)
    

def get_session():
    with Session(engine) as session:
        yield session