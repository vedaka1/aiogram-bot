import logging

import google.generativeai as genai
from aiogram import md
from google.api_core.exceptions import FailedPrecondition

from models import User
from utils.config import settings

logger = logging.getLogger()
gemini = genai
gemini.configure(api_key=settings.API_KEY_GEMINI)
model = gemini.GenerativeModel("gemini-pro")


class GeminiAI:
    @staticmethod
    async def generate_response(user: User) -> str:
        try:
            response = await model.generate_content_async(user.messages)
            user.messages.append({"role": "model", "parts": [response.text]})
            response = md.unparse(response.text)
            response = response.replace("\`\`\`", "```")
            return response
        except Exception as e:
            logger.error("User: %s, info: %s", user.id, e)
            return False

    @staticmethod
    def create_message(message):
        """Adds the user's message to the message list"""
        return {"role": "user", "parts": [message]}

    @staticmethod
    def _test_access() -> bool:
        try:
            model.generate_content("Hello")
            return True
        except FailedPrecondition:
            logger.error("Gemini not available. Setting status to False")
            return False
