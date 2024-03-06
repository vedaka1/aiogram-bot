import logging

from aiogram import Bot, F, Router, filters, types

from resources.chatgpt import ChatGPT, FreeChatGPT
from resources.database import Database
from resources.gemini import GeminiAI

logger = logging.getLogger()
router = Router()
db = Database()
chats = {}  # Users chats
available_models = {
    "Gemini": GeminiAI._test_access(),
    # 'ChatGPT': ChatGPT._test_access(),
    "FreeChatGPT": True,
}


@router.message(filters.Command("start"))
async def cmd_start(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    username = message.from_user.username
    await db.add_user(user_id, username)
    logger.info(f"New user: {user_id}!")
    await bot.send_message(
        chat_id=426826549, text=f"New user _{username}_\!", parse_mode="MarkDownV2"
    )
    await message.answer(
        "Привет!\n"
        + "Доступные команды:\n"
        + " /start_chat запускает ChatGPT\n"
        + " /end_chat отключает ChatGPT\n"
        + " /last_chapters отправляет последние главы новеллы"
    )


@router.message(filters.Command("start_chat"))
async def cmd_start_chat(message: types.Message):
    user_id = message.from_user.id
    await db.set_echo_mode(
        user_id, True
    )  # Включает режим echo_mode у текущего пользователя
    await message.answer("ChatGPT mode enabled")
    await cmd_select_model(message)


@router.message(filters.Command("end_chat"))
async def cmd_end_chat(message: types.Message):
    user_id = message.from_user.id
    await db.set_echo_mode(
        user_id, False
    )  # Отключает режим echo_mode у текущего пользователя
    if user_id in chats:
        chats.pop(user_id)
    await message.answer("ChatGPT mode disabled")


@router.message(lambda m: m.from_user.id not in chats)
async def check_model(message: types.Message):
    if await db.get_user_mode(message.from_user.id):
        await cmd_select_model(message)


@router.message(filters.Command("select_model"))
async def cmd_select_model(message: types.Message):
    user_id = message.from_user.id
    buttons = [
        [
            types.InlineKeyboardButton(
                text=model, callback_data=f"selectModel_{user_id}_{model}"
            )
        ]
        for model in available_models
        if available_models[model]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer("Выберите модель", reply_markup=keyboard)


@router.message(
    lambda m: m.from_user.id in chats
)  # Обрабатывается если у пользователя установлен режим echo_mode = True
async def echo(message: types.Message):
    user_id = message.from_user.id
    logger.info('User: %s, message: "%s"', user_id, message.text)
    chats[user_id].append_message(message.text)
    msg = await message.answer(text="<i>Waiting</i> \U0001F551")
    response = await chats[user_id].generate_response()
    if response:
        await msg.edit_text(response, parse_mode="MarkDownV2")
    else:
        buttons = [
            [
                types.InlineKeyboardButton(
                    text="Попробовать снова", callback_data=f"tryAgain_{user_id}"
                )
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        await msg.edit_text(
            "\U00002757 _Не удалось получить ответ_",
            parse_mode="MarkDownV2",
            reply_markup=keyboard,
        )


@router.callback_query(F.data.startswith("tryAgain_"))
async def try_again_callback(callback: types.CallbackQuery, bot: Bot):
    data = callback.data.split("_")
    user_id = int(data[1])
    chats[user_id].clear_history()
    await callback.message.edit_text(text="<i>Waiting</i> \U0001F551")
    response = await chats[user_id].generate_response()
    await callback.message.delete()
    if response:
        await callback.message.answer(response, parse_mode="MarkDownV2")
    else:
        await bot.send_message(
            chat_id=426826549,
            text=f"AI Error from _{user_id}_",
            parse_mode="MarkDownV2",
        )
        await callback.message.answer(
            "\U00002757 _Не удалось получить ответ, попробуйте позднее_",
            parse_mode="MarkDownV2",
        )


@router.callback_query(F.data.startswith("selectModel_"))
async def select_model_callback(callback: types.CallbackQuery):
    data = callback.data.split("_")
    user_id, choice = int(data[1]), data[2]
    if choice == "Gemini":
        chats[user_id] = GeminiAI(user_id)
    else:
        chats[user_id] = FreeChatGPT(user_id)
    await callback.message.edit_text(text=f"Текущая модель: {choice}")
