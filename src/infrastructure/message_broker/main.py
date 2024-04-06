from typing import AsyncGenerator

import aio_pika
from aio_pika.pool import Pool

from infrastructure.message_broker.factories import ChannelFactory, ConnectionFactory


def build_rq_connection_pool(
    url: str,
) -> AsyncGenerator[Pool[aio_pika.abc.AbstractConnection], None]:
    rq_connection_pool = Pool(ConnectionFactory(url).get_connection, max_size=10)
    return rq_connection_pool


def build_rq_channel_pool(
    rq_connection_pool: Pool[aio_pika.abc.AbstractConnection],
) -> AsyncGenerator[Pool[aio_pika.abc.AbstractChannel], None]:
    rq_channel_pool = Pool(ChannelFactory(rq_connection_pool).get_channel, max_size=100)
    return rq_channel_pool


async def build_rq_channel(
    rq_channel_pool: Pool[aio_pika.abc.AbstractChannel],
) -> AsyncGenerator[aio_pika.abc.AbstractChannel, None]:
    async with rq_channel_pool.acquire() as channel:
        yield channel
        channel.transaction()


async def build_rq_transaction(
    rq_channel: aio_pika.abc.AbstractChannel,
) -> aio_pika.abc.AbstractTransaction:
    rq_transaction = rq_channel.transaction()
    await rq_transaction.select()
    return rq_transaction
