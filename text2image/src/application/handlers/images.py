import json

from aiogram import Bot, types

from domain.messages.message import Message
from infrastructure.models.kadinsky import text2image


async def generate_image(message: Message, bot: Bot) -> None:
    msg = await bot.send_message(
        chat_id=message.user_id, text="<i>Waiting</i> \U0001F551"
    )
    try:
        response = await text2image.generate_response(message.prompt)
        image = types.BufferedInputFile(
            file=response["image_base64"], filename=response["image_id"]
        )
        await msg.delete()
    except:
        await msg.edit_text("Ошибка, попробуйте позднее")
        bot.send_message(
            chat_id=426826549,
            text=f"\U00002757 Image generation error from user _{message.user_id}_",
            parse_mode="MarkDownV2",
        )
    await bot.send_photo(chat_id=message.user_id, photo=image, caption=message.prompt)
