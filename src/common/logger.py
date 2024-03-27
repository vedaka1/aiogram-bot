import logging
from functools import lru_cache
from logging import Logger


@lru_cache(1)
def init_logger() -> Logger:
    logging.basicConfig(
        # filename="log.log",
        level=logging.INFO,
        encoding="UTF-8",
        format="%(asctime)s %(levelname)s: %(message)s",
    )
    logger = logging.getLogger()
    return logger
