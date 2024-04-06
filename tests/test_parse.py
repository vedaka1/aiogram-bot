import pytest

from src.logic.novel.parse import *


@pytest.mark.asyncio
async def test_get_last_chapters():
    result = await get_last_chapters()
    assert isinstance(result, list)
    assert len(result) == 5
    for item in result:
        assert isinstance(item, dict)
        assert len(item) == 2
