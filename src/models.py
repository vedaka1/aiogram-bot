import asyncio

from resources.database import db


class User:
    def __init__(self, id: int):
        self.id = id
        self.messages = []
        self.model = None

    def add_message(self, message):
        """Adds the user's message to the message list"""
        self.messages.append(self.model.create_message(message))

    def clear_messages(self):
        self.messages = [self.messages[-1]]

    def set_model(self, model):
        self.messages = []
        self.model = model

    async def generate_response(self) -> str:
        return await self.model.generate_response(self)
