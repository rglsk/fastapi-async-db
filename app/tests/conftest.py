from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.db.base import database
from app.main import app


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    await database.connect()
    yield
    await database.disconnect()


@pytest.fixture()
async def async_client() -> AsyncGenerator:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
