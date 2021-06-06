from fastapi import APIRouter

from app.api.routes import hello, articles

api_router = APIRouter()
api_router.include_router(hello.router, prefix="/hello")

articles_router = APIRouter()
articles_router.include_router(articles.router, prefix="/articles")
