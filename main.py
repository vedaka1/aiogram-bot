import asyncio, logging, os, traceback
from aiogram import Bot, Dispatcher, types, filters, F, html, md
from aiogram.utils import formatting
from resources import parse, config
from resources.chatgpt import ChatGPT
from resources.database import Database


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
db = Database()
chats = {} # Хранит чаты пользователей

async def main():
    await dp.start_polling(bot)


@dp.message(filters.Command("start_chat"))
async def cmd_start_chat(message: types.Message):
    user_id = message.from_user.id
    db.add_user(user_id)
    db.set_echo_mode(user_id, True) # Включает режим echo_mode у текущего пользователя
    await message.answer("ChatGPT mode enabled")


@dp.message(filters.Command("end_chat"))
async def cmd_end_chat(message: types.Message):
    global chats
    user_id = message.from_user.id
    db.set_echo_mode(user_id, False) # Отключает режим echo_mode у текущего пользователя
    if user_id in chats:
        chats.pop(user_id)
    await message.answer("ChatGPT mode disabled")


@dp.message(filters.Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    db.add_user(user_id)
    await message.answer("Привет!\n" + "Доступные команды:\n  /start_chat запускает ChatGPT\n  /end_chat отключает ChatGPT\n  /last_chapters отправляет последние главы новеллы", parse_mode="HTML")


@dp.message(filters.Command("last_chapters"))
async def get_chapters(message: types.Message):
    chapters = parse.get_last_chapters('https://readlightnovel.app/the-beginning-after-the-end-535558')
    buttons = [
        [
            types.InlineKeyboardButton(text=chapters[0][:7], callback_data=f"chapter_{chapters[0][3:6]}"), 
            types.InlineKeyboardButton(text=chapters[1][:7], callback_data=f"chapter_{chapters[1][3:6]}")
        ],
        [
            types.InlineKeyboardButton(text=chapters[2][:7], callback_data=f"chapter_{chapters[2][3:6]}"),
            types.InlineKeyboardButton(text=chapters[3][:7], callback_data=f"chapter_{chapters[3][3:6]}")
        ],
        [types.InlineKeyboardButton(text=chapters[4][:7], callback_data=f"chapter_{chapters[4][3:6]}")]
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer("<a href='https://readlightnovel.app/the-beginning-after-the-end-535558'>The Beginning After The End</a>\nChoose chapter to translate:", reply_markup=keyboard)


@dp.callback_query(F.data.startswith("chapter_"))
async def get_chapter_translate(callback: types.CallbackQuery):
    number = callback.data.split("_")[1]
    try:
        if not os.path.exists(f'translated/{number}.txt'):
            msg = await callback.message.answer("<i>Waiting for translate</i> \U0001F551")
            parse.get_chapter_text(f'https://readlightnovel.app/the-beginning-after-the-end-535558/chapter-{number}', number)
            await bot.delete_message(msg.chat.id, msg.message_id)
        file = types.FSInputFile(f'translated/{number}.txt')
        await callback.message.answer_document(file)
    except:
        await callback.message.answer("\U00002757 <i>Translation error, try again later</i>")
        logger.error(f'User: {callback.from_user.id}, info: {traceback.format_exc()}')


@dp.message(F.text.contains("CH"))
async def get_chapter_translate(message: types.Message):
    number = message.text[3:]
    try:
        if not os.path.exists(f'translated/{number}.txt'):
            await message.answer("<i>Waiting for translate</i> \U0001F551")
            parse.get_chapter_text(f'https://readlightnovel.app/the-beginning-after-the-end-535558/chapter-{number}', number)
        file = types.FSInputFile(f'translated/{number}.txt')
        await message.answer_document(file)
    except:
        await message.answer("\U00002757 <i>Translation error, try again later</i>")
        logger.error(f'User: {message.from_user.id}, info: {traceback.format_exc()}')


@dp.message(lambda m: db.get_user_mode(m.from_user.id)) # Обрабатывается если у пользователя установлен режим echo_mode = True
async def echo(message: types.Message):
    global chats
    user_id = message.from_user.id
    logger.info(f'User: {user_id}, message: "{message.text}"',)
    if user_id not in chats:
        chats[user_id] = ChatGPT()
    chats[user_id].append_message(message.text)
    msg = await bot.send_message(text = f"<i>Waiting</i> \U0001F551", chat_id= message.chat.id)
    try: 
        response = chats[user_id].response_completion(message.from_user.id)
        response = md.unparse(response)
        response = response.replace('\`\`\`', '```')
        await bot.edit_message_text(response, message_id= msg.message_id, chat_id= msg.chat.id, parse_mode="MarkDownV2")
    except:
        chats[user_id].clear_history()
        logger.error(f'User: {user_id}, info: {traceback.format_exc()}')
        await bot.edit_message_text(text = "\U00002757 <i>Token limit exceeded, clearing messsages list and restarting</i>", message_id= msg.message_id, chat_id= msg.chat.id)


if __name__ == "__main__":
    logging.basicConfig(filename='log_file.log',
                        level=logging.INFO,
                        encoding='UTF-8',
                        format='%(asctime)s %(levelname)s: %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    asyncio.run(main())