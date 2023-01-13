import warnings

import pytest
from httpx import AsyncClient
from trio import TrioDeprecationWarning

from src.main import app

warnings.filterwarnings(action="ignore", category=TrioDeprecationWarning)


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as server_client:
        yield server_client
