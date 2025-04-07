from fastapi.testclient import TestClient
from sqlmodel import Session, select

from app.models import Test

def test_get_root(
        client: TestClient, session: Session
) -> None:
    name = "медвед"
    response = client.get(f"/?name={name}")
    json = response.json()
    hello = session.exec(select(Test)).first().hello
    assert response.is_success is True
    assert json
    assert json == {"message": f"{hello}{name}"}

def test_get_root_empty_name(
        client: TestClient, session: Session
) -> None:
    response = client.get("/")
    json = response.json()
    hello = session.exec(select(Test)).first().hello
    assert response.is_success is True
    assert json