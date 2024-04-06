import logging
import traceback
from contextlib import asynccontextmanager
from functools import lru_cache
from logging import Logger
from typing import Any, AsyncGenerator

import asyncpg
from asyncpg.connection import Connection
from httpx import AsyncClient

from infrastructure.message_broker.main import (
    build_rq_channel,
    build_rq_channel_pool,
    build_rq_connection_pool,
    build_rq_transaction,
)
from infrastructure.message_broker.message_broker import MessageBroker, RabbitMQ
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


def init_async_client(base_url: str = "", headers: dict = None) -> AsyncClient:
    client = AsyncClient(base_url=base_url, headers=headers)
    return client


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


connection_pool = build_rq_connection_pool(settings.RABBITMQ_URL)
channel_pool = build_rq_channel_pool(connection_pool)


async def init_message_broker():
    broker = MessageBroker(channel_pool)
    return broker
