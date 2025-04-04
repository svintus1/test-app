from collections.abc import Generator
import pytest
from fastapi.testclient import TestClient
from sqlmodel import delete, Session

from app.main import app
from app.core.database import engine, init_db

@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session", autouse=True)
def session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        init_db()
        yield session