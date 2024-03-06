import logging

import google.generativeai as genai
from aiogram import md
from google.api_core.exceptions import FailedPrecondition

from resources.config import settings

logger = logging.getLogger()
gemini = genai
gemini.configure(api_key=settings.API_KEY_GEMINI)
model = gemini.GenerativeModel("gemini-pro")


class GeminiAI:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.messages = []

    async def generate_response(self) -> str:
        try:
            response = await model.generate_content_async(self.messages)
            self.messages.append({"role": "model", "parts": [response.text]})
            response = md.unparse(response.text)
            response = response.replace("\`\`\`", "```")
            return response
        except Exception as e:
            logger.error("User: %s, info: %s", self.user_id, e)
            return False

    def append_message(self, message):
        """Adds the user's message to the message list"""
        self.messages.append({"role": "user", "parts": [message]})

    def clear_history(self):
        self.messages = [self.messages[-1]]

    @classmethod
    def _test_access(self) -> bool:
        try:
            model.generate_content("Hello")
            return True
        except FailedPrecondition:
            logger.error("Gemini not available. Setting status to False")
            return False
