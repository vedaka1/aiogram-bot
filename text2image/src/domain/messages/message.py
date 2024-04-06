from dataclasses import dataclass


@dataclass
class Message:
    message_id: str
    user_id: str
    prompt: str
