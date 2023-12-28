import json
import pytest
from httpx import AsyncClient, _status_codes


@pytest.mark.asyncio
async def test_post_request():
    url = "http://localhost:8080"
    payload = json.dumps(
        {
            "data": "Hello world!",
        }
    )

    async with AsyncClient() as client:
        response = await client.post(url, content=payload)
        print(response.content)
        print(response.headers)

    assert response.status_code == _status_codes.codes.NO_CONTENT  # 204
