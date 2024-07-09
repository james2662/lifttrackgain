from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

from endpoints.admin.create_user import create_user