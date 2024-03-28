import logging
import traceback
from contextlib import asynccontextmanager
from functools import lru_cache
from logging import Logger
from typing import Any, AsyncGenerator

import asyncpg
from asyncpg.connection import Connection

from infrastructure.repositories.user import UserRepository
from settings import settings


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


@asynccontextmanager
async def create_connection() -> AsyncGenerator[Any, Connection]:
    try:
        conn: Connection = await asyncpg.connect(settings.DB_URL)
        yield conn
    except:
        print(traceback.format_exc())
    finally:
        await conn.close()


user_repository = UserRepository(connection=create_connection, db_schema="tg_bot")
