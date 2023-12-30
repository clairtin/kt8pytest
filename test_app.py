import aiohttp
import pytest
import asyncio
from app import get_json


@pytest.mark.asyncio
async def test_get_json_valid_url():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = await get_json(url)
    assert "userId" in result
    assert "id" in result
    assert "title" in result
    assert "completed" in result

@pytest.mark.asyncio
async def test_get_json_invalid_url():
    url = "https://example.com/nonexistent"
    with pytest.raises(aiohttp.ClientResponseError):
        await get_json(url)

