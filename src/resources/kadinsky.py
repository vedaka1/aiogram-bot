import asyncio
import base64
import json

from httpx import AsyncClient, Client, Response

from resources.config import settings


class Text2ImageAPI:

    def __init__(self):
        self.__AUTH_HEADERS = {
            "X-Key": f"Key {settings.API_KEY_KADINSKY}",
            "X-Secret": f"Secret {settings.API_SECRET_KEY_KADINSKY}",
        }
        self.client = AsyncClient(
            base_url="https://api-key.fusionbrain.ai/", headers=self.__AUTH_HEADERS
        )
        self.model_id = self.__get_model()

    def __get_model(self):
        with Client() as client:
            response: Response = client.get(
                "https://api-key.fusionbrain.ai/key/api/v1/models",
                headers=self.__AUTH_HEADERS,
            )
            data = response.json()
            return data[0]["id"]

    async def generate_response(self, prompt, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {"query": f"{prompt}"},
        }
        data = {
            "params": (None, json.dumps(params), "application/json"),
        }
        response: Response = await self.client.post(
            "key/api/v1/text2image/run", params={"model_id": self.model_id}, files=data
        )
        data = response.json()
        return data["uuid"]

    async def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = await self.client.get(
                "key/api/v1/text2image/status/" + request_id
            )
            data = response.json()
            if data["status"] == "DONE":
                return data["images"]

            attempts -= 1
            await asyncio.sleep(delay)


text2image = Text2ImageAPI()


# async def test():
#     uuid = await text2image.generate_response(
#         "сакура растет посреди разрушенной и мрачной улицы в стиле киберпанк"
#     )
#     images = await text2image.check_generation(uuid)
#     image_base64 = images[0]
#     image_data = base64.b64decode(image_base64)
#     with open("image.txt", "w") as file:
#         file.write(image_base64 + "\n")
#         file.write(image_data + "\n")


# asyncio.run(test())