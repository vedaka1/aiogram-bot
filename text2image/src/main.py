import asyncio
import json

import aio_pika
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from application.handlers.images import generate_image
from infrastructure.ioc import init_logger
from infrastructure.messages.converters import convert_rq_message
from settings import settings


async def on_message(message: aio_pika.abc.AbstractIncomingMessage) -> None:
    await generate_image(convert_rq_message(message), bot)


async def main():
    connection = await aio_pika.connect(settings.RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("textToImage")
        await queue.consume(on_message, no_ack=True)
        logger.info(" [*] Waiting for messages")
        await asyncio.Future()


if __name__ == "__main__":
    logger = init_logger()
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    asyncio.run(main())
