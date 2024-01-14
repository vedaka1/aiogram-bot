import logging
from aiogram import md
import google.generativeai as genai
from resources.config import API_KEY_GEMINI


logger = logging.getLogger()


class GeminiAI:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.api_key = API_KEY_GEMINI
        self.messages = []
        self.genai = genai
        self.genai.configure(api_key=self.api_key)
        self.model: genai.GenerativeModel = self.genai.GenerativeModel('gemini-pro')

    async def generate_response(self):
        try:
            response = await self.model.generate_content_async(self.messages)
            self.messages.append({'role': 'model', 'parts': [response.text]})
            response = md.unparse(response.text)
            response = response.replace("\`\`\`", "```")
            return response
        except Exception as e:
            logger.error('User: %s, info: %s', self.user_id, e)
            return False

    def append_message(self, message):
        """Adds the user's message to the message list"""
        self.messages.append({"role": "user", "parts": [message]})

    def clear_history(self):
        self.messages = [self.messages[-1]]
