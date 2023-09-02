import asyncio, logging, requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types, filters, utils

import config, parse
# from handler import router

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

async def main():
    await dp.start_polling(bot)

# @dp.message_handler()
# async def start(message: types.Message):
#     await message.answer('hello!')

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Последние главы")]
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("The Beginning After the End\nLight novel", reply_markup=keyboard)

@dp.message_handler(filters.Text('Последние главы'))
async def get_chapters(message: types.Message):
    chapters = parse.get_data('https://readlightnovel.app/the-beginning-after-the-end-535558')
    text = ''
    kb = []
    for chapter in chapters:
        kb.append([types.KeyboardButton(text=chapter[:7])])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    for item in chapters:
        text += (item +'\n')
    await message.answer(text, reply_markup=keyboard)

@dp.message_handler(filters.Text(contains='CH'))
async def get_chapter_translate(message: types.Message):
    number = message.text[3:]
    kb = [
        [types.KeyboardButton(text="Последние главы")]
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Подождите, идет перевод")
    parse.get_text(f'https://readlightnovel.app/the-beginning-after-the-end-535558/chapter-{number}', number)
    await message.reply_document(open(f'translated/{number}.txt', 'rb'), reply_markup=keyboard)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())