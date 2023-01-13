import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_server_status(client: AsyncClient):
    response = await client.get("/server_status")
    assert response.status_code == 200
    assert response.json() == {"status": "All great, all nice!"}
