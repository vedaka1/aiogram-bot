import logging
from dataclasses import dataclass, field

import google.generativeai as genai
from google.api_core.exceptions import FailedPrecondition

from common.logger import init_logger
from config import settings
from domain.common.base import BaseTextModel
from domain.common.response import Response
from domain.users.user import User


def init_gemini() -> genai.GenerativeModel:
    gemini = genai
    gemini.configure(api_key=settings.API_KEY_GEMINI)
    model = gemini.GenerativeModel("gemini-pro")
    return model


@dataclass
class GeminiAI(BaseTextModel):

    logger: logging.Logger = field(default=init_logger(), init=False)
    model: genai.GenerativeModel = field(default=init_gemini(), init=False)

    async def generate_response(self, user: User) -> str:
        try:
            result = await self.model.generate_content_async(user.messages)
            user.messages.append({"role": "model", "parts": [result.text]})
            response = Response(result.text)
            return response.value
        except Exception as e:
            self.logger.error("User: %s, info: %s", user.id, e)
            return False

    @staticmethod
    def create_message(text) -> dict[str, str]:
        """Adds the user's message to the message list"""
        return {"role": "user", "parts": [text]}

    @classmethod
    def _test_access(cls) -> bool:
        try:
            cls.model.generate_content("Hello")
            return True
        except FailedPrecondition:
            cls.logger.error("Gemini not available. Setting status to False")
            return False
