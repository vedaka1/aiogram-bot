import json
import logging
from dataclasses import dataclass, field

import aio_pika
from aio_pika.abc import AbstractChannel
from aio_pika.pool import Pool

from .message import Message

logger = logging.getLogger(__name__)


@dataclass
class MessageBroker:
    _channel_pool: AbstractChannel

    async def publish_message(self, message: Message, routing_key: str) -> None:
        rq_message = self.build_message(message)
        await self._publish_message(rq_message, routing_key)

    @staticmethod
    def build_message(message: Message) -> aio_pika.Message:
        return aio_pika.Message(
            body=bytes(
                json.dumps(dict(message_type=message.message_type, data=message.data)),
                encoding="utf-8",
            ),
            message_id=str(message.id),
            content_type="application/json",
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
            headers={},
        )

    async def _publish_message(
        self, rq_message: aio_pika.Message, routing_key: str
    ) -> None:
        async with self._channel_pool.acquire() as channel:
            await channel.default_exchange.publish(rq_message, routing_key=routing_key)
        logger.debug("Message sent", extra={"rq_message": rq_message})


@dataclass
class RabbitMQ:
    url: str
    _connection: aio_pika.Connection = field(default=None, init=False)

    async def connect(self) -> None:
        self._connection = await aio_pika.connect_robust(self.url)

    async def get_channel(self) -> AbstractChannel:
        return await self._connection.channel()
