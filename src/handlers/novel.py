import logging
import os
import traceback

from aiogram import F, Router, filters, types

from utils import parse

logger = logging.getLogger()
router = Router()
WEBSITE = "https://readlitenovel.com/the-beginning-after-the-end-535558"


@router.message(filters.Command("last_chapters"))
async def get_chapters(message: types.Message):
    chapters = parse.get_last_chapters()
    buttons = [
        [
            types.InlineKeyboardButton(
                text=f"CH {chapters[0][0]}", callback_data=f"chapter_{chapters[0][0]}"
            ),
            types.InlineKeyboardButton(
                text=f"CH {chapters[1][0]}", callback_data=f"chapter_{chapters[1][0]}"
            ),
        ],
        [
            types.InlineKeyboardButton(
                text=f"CH {chapters[2][0]}", callback_data=f"chapter_{chapters[2][0]}"
            ),
            types.InlineKeyboardButton(
                text=f"CH {chapters[3][0]}", callback_data=f"chapter_{chapters[3][0]}"
            ),
        ],
        [
            types.InlineKeyboardButton(
                text=f"CH {chapters[4][0]}", callback_data=f"chapter_{chapters[4][0]}"
            )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(
        f"<a href='{WEBSITE}'>The Beginning After The End</a>\nChoose chapter to translate:",
        reply_markup=keyboard,
    )


@router.callback_query(F.data.startswith("chapter_"))
async def get_chapter_translate(callback: types.CallbackQuery):
    number = callback.data.split("_")[1]
    buttons = [
        [
            types.InlineKeyboardButton(
                text="EN", callback_data=f"chapterlang_{number}_en"
            ),
            types.InlineKeyboardButton(
                text="RU", callback_data=f"chapterlang_{number}_ru"
            ),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(F.data.startswith("chapterlang_"))
async def get_chapter_translate_lang(callback: types.CallbackQuery):
    data = callback.data.split("_")
    number, lang = data[1], data[2]
    try:
        if not os.path.exists(f"./translated/{number}_{lang}.txt"):
            msg = await callback.message.answer(
                "<i>Waiting for translate</i> \U0001F551"
            )
            parse.get_chapter_text(f"{WEBSITE}/chapter-{number}", number, lang)
            await msg.delete()
        file = types.FSInputFile(f"./translated/{number}_{lang}.txt")
        await callback.message.answer_document(file)
        await callback.message.delete()
    except:
        await callback.message.answer(
            "\U00002757 <i>Translation error, try again later</i>"
        )
        logger.error(
            f"On callback from user: {callback.from_user.id}, \
            info: {traceback.format_exc()}"
        )


@router.message(F.text.contains("CH"))
async def get_custom_chapter_translate(message: types.Message):
    number = message.text[3:]
    try:
        if not os.path.exists(f"translated/{number}.txt"):
            await message.answer("<i>Waiting for translate</i> \U0001F551")
            parse.get_chapter_text(f"{WEBSITE}/chapter-{number}", number, "ru")
        file = types.FSInputFile(f"translated/{number}.txt")
        await message.answer_document(file)
    except:
        await message.answer("\U00002757 <i>Translation error, try again later</i>")
        logger.error(f"User: {message.from_user.id}, info: {traceback.format_exc()}")
