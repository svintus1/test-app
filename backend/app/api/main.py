from fastapi import APIRouter

from app.api.routes import root

api_router = APIRouter()
api_router.include_router(root.router)