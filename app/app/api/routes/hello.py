from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello() -> str:
    return "OK"
