from fastapi import APIRouter

router = APIRouter(
    prefix="/oauth",
    tags=["oauth"],
)