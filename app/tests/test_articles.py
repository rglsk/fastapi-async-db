import pytest
from httpx import AsyncClient

from app.db.repositories.articles import ArticleRepository
from app.models.articles import ArticleIn, ArticleOut

pytestmark = pytest.mark.asyncio


@pytest.fixture()
def article_data() -> ArticleIn:
    return ArticleIn(title="Test article", slug="Test slug", text="Test text")


async def test_articles_list_empty(async_client: AsyncClient):
    response = await async_client.get("/api/v1/articles")

    assert response.json() == []


async def test_articles_list(async_client: AsyncClient, article_data: ArticleIn):
    repo = ArticleRepository()
    article: ArticleOut = await repo.create(article_data)
    response = await async_client.get("/api/v1/articles")

    assert response.json() == [
        {
            "id": str(article.id),
            "created_at": article.created_at.isoformat(),
            "slug": article.slug,
            "text": article.text,
            "title": article.title,
        }
    ]
