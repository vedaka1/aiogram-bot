from aiogram import Router, types, filters
from aiogram import types, filters
from resources.database import Database
from resources.chatgpt import FreeChatGPT
import logging


logger = logging.getLogger()
router = Router()
db = Database()
chats = {}  # Users chats


@router.message(filters.Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    db.add_user(user_id, username)
    logger.info(f'New user: {user_id}!')
    await message.answer("Привет!\n" + "Доступные команды:\n  /start_chat запускает ChatGPT\n  /end_chat отключает ChatGPT\n  /last_chapters отправляет последние главы новеллы", parse_mode="HTML")

@router.message(filters.Command("start_chat"))
async def cmd_start_chat(message: types.Message):
    user_id = message.from_user.id
    db.set_echo_mode(user_id, True) # Включает режим echo_mode у текущего пользователя
    await message.answer("ChatGPT mode enabled")


@router.message(filters.Command("end_chat"))
async def cmd_end_chat(message: types.Message):
    global chats
    user_id = message.from_user.id
    db.set_echo_mode(user_id, False) # Отключает режим echo_mode у текущего пользователя
    if user_id in chats:
        chats.pop(user_id)
    await message.answer("ChatGPT mode disabled")


@router.message(lambda m: db.get_user_mode(m.from_user.id)) # Обрабатывается если у пользователя установлен режим echo_mode = True
async def echo(message: types.Message):
    global chats
    user_id = message.from_user.id
    logger.info(f'User: {user_id}, message: "{message.text}"',)
    if user_id not in chats:
        chats[user_id] = FreeChatGPT(user_id)
    chats[user_id].append_message(message.text)
    msg = await message.answer(text = f"<i>Waiting</i> \U0001F551")
    response = await chats[user_id].run_all()
    await msg.edit_text(response, parse_mode="MarkDownV2")
