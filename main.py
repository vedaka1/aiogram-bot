import asyncio, logging, os, traceback
from aiogram import Bot, Dispatcher, types, filters, F, html
from resources import parse, config
from resources.chatgpt import ChatGPT


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
echo_mode = True
chat = ChatGPT()

async def main():
    await dp.start_polling(bot)

@dp.message(filters.Command("start-chat"))
async def cmd_start(message: types.Message):
    global echo_mode
    echo_mode = True
    await message.answer("ChatGPT mode enabled")

@dp.message(filters.Command("end-chat"))
async def cmd_start(message: types.Message):
    global echo_mode
    echo_mode = False
    await message.answer("ChatGPT mode disabled")


@dp.message(filters.Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Последние главы")]
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("The Beginning After the End\nLight novel", reply_markup=keyboard)

@dp.message(F.text.lower() == "последние главы")
async def get_chapters(message: types.Message):
    chapters = parse.get_last_chapters('https://readlightnovel.app/the-beginning-after-the-end-535558')
    text = ''
    kb = []
    for chapter in chapters:
        kb.append([types.KeyboardButton(text=chapter[:7])])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    for item in chapters:
        text += (f'<a href="{item[10:]}">{item[1:7]}</a>\n')
    print(text)
    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")

@dp.message(F.text.contains("CH"))
async def get_chapter_translate(message: types.Message):
    number = message.text[3:]
    kb = [
        [types.KeyboardButton(text="Последние главы")]
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    try:
        if not os.path.exists(f'C:/Projects/Python/aiogram-bot/translated/{number}.txt'): 
            await message.answer("Подождите, идет перевод")
            parse.get_chapter_text(f'https://readlightnovel.app/the-beginning-after-the-end-535558/chapter-{number}', number)
        file = types.FSInputFile(f'C:/Projects/Python/aiogram-bot/translated/{number}.txt')
        await message.answer_document(file, reply_markup=keyboard)
    except:
        await message.answer("Возникла ошибка при переводе, попробуйте позже", reply_markup=keyboard)
        print(traceback.format_exc())

@dp.message(lambda m: echo_mode)
async def echo(message: types.Message):
    chat.append_message(message.text)
    try:
        response = chat.response_completion()
        await message.answer(f"{html.quote(response)}")
    except:
        print(traceback.format_exc())   

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())