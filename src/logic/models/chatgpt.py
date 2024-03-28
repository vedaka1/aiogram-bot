import asyncio
import logging
from dataclasses import dataclass, field

import g4f
import openai

from domain.common.response import Response
from domain.neuro.model import BaseTextModel
from domain.users.user import User
from infrastructure.ioc import init_logger
from settings import settings

g4f.debug.logging = False
_providers = [
    # g4f.Provider.Aura,
    g4f.Provider.GeminiProChat,
    g4f.Provider.Koala,
    # g4f.Provider.Aichat,
    # g4f.Provider.ChatBase,
    # g4f.Provider.Bing,
    # g4f.Provider.GptGo,
    # g4f.Provider.You,
    # g4f.Provider.Yqcloud,
    # g4f.Provider.GPTalk,
    g4f.Provider.Hashnode,
    g4f.Provider.FreeGpt,
    g4f.Provider.ChatgptAi,
    g4f.Provider.Liaobots,
    g4f.Provider.Chatgpt4Online,
    g4f.Provider.ChatgptNext,
    g4f.Provider.ChatgptX,
    g4f.Provider.GptForLove,
    g4f.Provider.FlowGpt,
    g4f.Provider.GptTalkRu,
    g4f.Provider.Vercel,
]


@dataclass
class ChatGPT(BaseTextModel):
    """ChatGPT class for bot users"""

    logger: logging.Logger = field(default=init_logger(), init=False)
    client: openai.AsyncOpenAI = field(
        default=openai.AsyncOpenAI(api_key=settings.API_KEY_CHATGPT), init=False
    )
    model: str = "gpt-3.5-turbo"

    async def generate_response(self, user: User, append=True) -> str:
        """Creates a response from ChatGPT"""
        try:
            completion = await self.client.chat.completions.create(
                model=self.model, messages=user.messages, temperature=0.8
            )
            result = completion.choices[0].message.content
            if append:
                user.messages.append({"role": "assistant", "content": response})
            response = Response(result)
            return response.value
        except Exception as e:
            self.logger.error("User: %s, info: %s", user.id, e)
            return False

    @staticmethod
    def create_message(text) -> dict[str, str]:
        """Adds the user's message to the message list"""
        return {"role": "user", "content": text}

    @classmethod
    def _test_access(cls):
        client = openai.OpenAI(api_key=settings.API_KEY_CHATGPT)
        try:
            client.chat.completions.create(
                model=cls.model,
                messages={"role": "user", "content": "Hello"},
                temperature=0.8,
            )
            return True
        except Exception:
            cls.logger.error("ChatGPT not available. Setting status to False")
            return False


@dataclass
class FreeChatGPT(BaseTextModel):
    """FreeChatGPT class for bot users"""

    logger: logging.Logger = field(default=init_logger(), init=False)

    @classmethod
    async def _run_provider(
        cls, provider: g4f.Provider.BaseProvider, user_messages: list[dict], logs=False
    ):
        """Runs the chat provider"""
        try:
            response = await g4f.ChatCompletion.create_async(
                model=g4f.models.default,
                messages=user_messages,
                provider=provider,
            )
            return response

        except Exception as e:
            if logs:
                cls.logger.error("Provider: %s, info: %s", provider.__name__, e)
            return None

    async def generate_response(self, user: User) -> str:
        """Generates responses from different providers"""
        calls = [self._run_provider(provider, user.messages) for provider in _providers]
        responses = await asyncio.gather(*calls)
        result = [
            response
            for response in responses
            if response is not None and response != ""
        ]
        if result:
            user.messages.append({"role": "assistant", "content": result[0]})
            response = Response(result[0])
            self.logger.info('User: %s, chat_response: "%s"', user.id, response.value)
            return response.value
        self.logger.error("User: %s, info: %s", user.id, responses)
        return False

    @staticmethod
    def create_message(message) -> dict[str, str]:
        """Adds the user's message to the message list"""
        return {"role": "user", "content": message}
