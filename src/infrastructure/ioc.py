import logging
import traceback
from contextlib import asynccontextmanager
from functools import lru_cache
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
from infrastructure.message_broker.message_broker import MessageBroker
from infrastructure.repositories.user import UserRepository
from logic.models.chatgpt import ChatGPT, FreeChatGPT
from logic.models.gemini import GeminiAI
from logic.models.gigachat import GigaChatAI
from settings import settings


@lru_cache(1)
def init_logger() -> logging.Logger:
    logging.basicConfig(
        # filename="log.log",
        level=logging.INFO,
        encoding="UTF-8",
        format="%(asctime)s %(levelname)s: %(message)s",
    )
    logger = logging.getLogger()
    return logger


def init_async_client(
    base_url: str = "", headers: dict = None, verify: bool = True
) -> AsyncClient:
    client = AsyncClient(base_url=base_url, headers=headers, verify=verify)
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


def init_models() -> dict:
    models = {
        "Gemini": {"model": GeminiAI(), "status": GeminiAI._test_access()},
        "ChatGPT": {"model": ChatGPT(), "status": ChatGPT._test_access()},
        "FreeChatGPT": {
            "model": FreeChatGPT(),
            "status": FreeChatGPT._test_access(),
        },
        "GigaChatAI": {
            "model": GigaChatAI(),
            "status": GigaChatAI._test_access(),
        },
    }
    return models
