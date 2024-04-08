from dataclasses import dataclass, field

from domain.neuro.model import BaseTextModel


@dataclass
class User:
    id: int
    messages: list[dict] = field(default_factory=list, init=False)
    model: BaseTextModel = field(default=None, init=False)

    def add_message(self, text: str) -> None:
        """Adds the user's message to the message list"""
        self.messages.append(self.model.create_message(text))

    def clear_messages(self) -> None:
        self.messages = [self.messages[-1]]

    def set_model(self, model) -> None:
        self.messages = []
        self.model: BaseTextModel = model

    async def generate_response(self) -> str:
        return await self.model.generate_response(self)
