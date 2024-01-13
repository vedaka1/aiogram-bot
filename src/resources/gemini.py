import logging
import asyncio
from aiogram import md
import google.generativeai as genai
from resources.config import API_KEY_GEMINI


logger = logging.getLogger()


class GeminiAI:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.API_KEY_GEMINI = API_KEY_GEMINI
        self.messages = []
        self.genai = genai
        self.genai.configure(api_key=self.API_KEY_GEMINI)

        self.model = self.genai.GenerativeModel('gemini-pro')

    async def create_response(self, message):
        try:
            response = await self.model.generate_content_async(message)
            response = md.unparse(response)
            response = response.replace("\`\`\`", "```")
            return response
        except Exception as e:
            logger.error('User: %s, info: %s', self.user_id, e)
            return "\U00002757 _Token limit exceeded\, clearing messsages list and restarting_"