import logging

from aiogram import Bot, Router, filters, types

from infrastructure.ioc import init_message_broker
from infrastructure.message_broker.message import Message
from infrastructure.message_broker.message_broker import MessageBroker

logger = logging.getLogger()
router = Router()


@router.message(filters.Command("imagine"))
async def generate_image(
    message: types.Message, command: filters.command.CommandObject
):
    user_id = message.from_user.id
    prompt = command.args
    broker: MessageBroker = await init_message_broker()
    message = Message(data={"user_id": user_id, "prompt": prompt})
    await broker.publish_message(message=message, routing_key="textToImage")

    # if command.args is None:
    #     await message.answer("Ошибка, не переданы аргументы")
    #     return
    # user_id = message.from_user.id
    # prompt = command.args
    # msg = await message.answer("<i>Waiting</i> \U0001F551")
    # try:
    #     response = await text2image.generate_response(prompt)
    #     # image_base64 = await text2image.check_generation(image_id)
    #     image = types.BufferedInputFile(
    #         file=response["image_base64"], filename=response["image_id"]
    #     )
    #     await msg.delete()
    # except:
    #     await msg.edit_text("Ошибка, попробуйте позднее")
    #     bot.send_message(
    #         chat_id=426826549,
    #         text=f"\U00002757 Image generation error from user _{user_id}_",
    #         parse_mode="MarkDownV2",
    #     )
    # await message.answer_photo(photo=image, caption=prompt)
