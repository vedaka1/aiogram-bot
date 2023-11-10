import os, traceback, logging
from aiogram import types, filters, F, Router
from resources import parse

logger = logging.getLogger()
router = Router()


@router.message(filters.Command("last_chapters"))
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


@router.callback_query(F.data.startswith("chapter_"))
async def get_chapter_translate(callback: types.CallbackQuery):
    number = callback.data.split("_")[1]
    buttons = [
        [
            types.InlineKeyboardButton(text='EN', callback_data=f"chapterlang_{number}_en"),
            types.InlineKeyboardButton(text='RU', callback_data=f"chapterlang_{number}_ru")
        ]
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(F.data.startswith("chapterlang_"))
async def get_chapter_translate(callback: types.CallbackQuery):
    data = callback.data.split("_")
    number, lang = data[1], data[2]
    try:
        if not os.path.exists(f'./translated/{number}_{lang}.txt'):
            msg = await callback.message.answer("<i>Waiting for translate</i> \U0001F551")
            parse.get_chapter_text(f'https://readlightnovel.app/the-beginning-after-the-end-535558/chapter-{number}', number, lang)
            await msg.message.delete()
        file = types.FSInputFile(f'./translated/{number}_{lang}.txt')
        await callback.message.answer_document(file)
        await callback.message.delete()
    except:
        await callback.message.answer("\U00002757 <i>Translation error, try again later</i>")
        logger.error(f'On callback from user: {callback.from_user.id}, info: {traceback.format_exc()}')


@router.message(F.text.contains("CH"))
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