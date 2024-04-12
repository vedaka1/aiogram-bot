import pytest

from src.logic.novel.parse import *


@pytest.mark.asyncio
async def test_get_last_chapters():
    result = await get_last_chapters()
    print(result)
    assert isinstance(result, list)
    assert len(result) == 5
    for item in result:
        assert isinstance(item, dict)
        assert len(item) == 2


@pytest.mark.asyncio
async def test_get_chapter_text():
    result = await get_chapter_text(
        "https://readlitenovel.com/the-beginning-after-the-end-535558/chapter-476",
        476,
        "ru",
    )
    print(result)
