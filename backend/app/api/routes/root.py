from fastapi import APIRouter, Depends, Query
from typing import Annotated
from sqlmodel import select

from app.models import Test
from app.core.database import get_session, Session
router = APIRouter()


# HTTP-эндпоинты
@router.get("/")
async def get_homepage(name: Annotated[str | None, Query()] = "test", session: Session = Depends(get_session)):
    test_data = session.exec(select(Test)).first()
    return {"message": f"{test_data.hello}{name}"}
