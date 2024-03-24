from src.utils.parse import *


def test_get_last_chapters():
    result = get_last_chapters()
    assert isinstance(result, list)
    assert len(result) == 5
    for sublist in result:
        assert isinstance(sublist, list)
        assert len(sublist) == 2
