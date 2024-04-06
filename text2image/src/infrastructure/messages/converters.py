import json

import aio_pika

from domain.messages.message import Message


def convert_rq_message(rq_message: aio_pika.abc.AbstractIncomingMessage) -> Message:
    json_data = bytes.decode(rq_message.body, encoding="utf-8")
    message = json.loads(json_data)
    return Message(
        message_id=rq_message.message_id,
        user_id=message["data"]["user_id"],
        prompt=message["data"]["prompt"],
    )
