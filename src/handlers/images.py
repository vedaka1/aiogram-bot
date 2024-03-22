import base64
import logging

from aiogram import Bot, F, Router, filters, types

from models import User
from resources.chatgpt import ChatGPT, FreeChatGPT
from resources.database import db
from resources.kadinsky import text2image

logger = logging.getLogger()
router = Router()


@router.message(filters.Command("imagine"))
async def generate_image(
    message: types.Message, command: filters.command.CommandObject
):
    if command.args is None:
        await message.answer("Ошибка, не переданы аргументы")
        return
    prompt = command.args
    msg = await message.answer("<i>Waiting</i> \U0001F551")
    image_id = await text2image.generate_response(prompt)
    image_binary = await text2image.check_generation(image_id)
    image = types.BufferedInputFile(
        file=base64.b64decode(image_binary[0]), filename=image_id
    )
    await msg.delete()
    await message.answer_photo(photo=image, caption=prompt)
