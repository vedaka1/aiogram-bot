import json
import logging
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

from httpx import AsyncClient

from domain.common.response import Response
from domain.neuro.model import BaseTextModel
from domain.users.user import User
from settings import settings


@dataclass
class GigaChatAI(BaseTextModel):

    logger: logging.Logger = field(default=logging.getLogger(), init=False)
    url: str = field(
        default="https://gigachat.devices.sberbank.ru/api/v1/chat/completions",
        init=False,
    )
    _access_token: str = field(default="", init=False)
    client: AsyncClient = field(
        default=AsyncClient(base_url="https://api-key.fusionbrain.ai/", verify=False),
        init=False,
    )
    auth_time: datetime = field(default=None, init=False)

    async def generate_response(self, user: User) -> str:
        await self.authenticate()
        try:
            payload = json.dumps(
                {
                    "model": "GigaChat",
                    "messages": [user.messages[-1]],
                    "temperature": 1,
                    "top_p": 0.1,
                    "n": 1,
                    "stream": False,
                    "max_tokens": 1024,
                    "repetition_penalty": 1,
                }
            )
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {self._access_token}",
            }
            response = await self.client.post(self.url, headers=headers, data=payload)
            message = response.json()["choices"][0]["message"]
            user.messages.append(message)
            response = Response(value=message["content"])
            return response.as_generic_type()

        except Exception as e:
            self.logger.error("User: %s, info: %s", user.id, e)
            return False

    async def authenticate(self) -> bool:
        if self.auth_time == None or datetime.now(
            timezone.utc
        ) >= self.auth_time + timedelta(minutes=25):
            self.logger.info("Authenticating GigaChat")
            try:
                url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
                payload = "scope=GIGACHAT_API_PERS"
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "application/json",
                    "RqUID": f"{uuid.uuid4()}",
                    "Authorization": f"Basic {settings.AUTH_DATA_SBER}",
                }
                response = await self.client.post(url, headers=headers, data=payload)
                self.auth_time = datetime.now(timezone.utc)
                self._access_token = response.json()["access_token"]

            except Exception as e:
                self.logger.error("GigaChat Auth Error %s", e)
                raise Exception("GigaChat Auth Error")

    @staticmethod
    def create_message(text: str) -> dict[str, str]:
        """Adds the user's message to the message list"""
        return {"role": "user", "content": text}

    @classmethod
    def _test_access(cls) -> bool:
        return True
