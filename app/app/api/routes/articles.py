from typing import List

from fastapi import APIRouter

from app.db.repositories.articles import ArticleRepository
from app.models.articles import ArticleOut

router = APIRouter()


@router.get("/")
async def articles_list() -> List[ArticleOut]:
    article_repo: ArticleRepository = ArticleRepository()
    articles = await article_repo.list()
    return articles
