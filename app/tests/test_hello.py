import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_hello(async_client: AsyncClient) -> None:
    response = await async_client.get("/api/v1/hello")

    assert response.status_code == 200
    assert response.content.decode() == '"OK"'
