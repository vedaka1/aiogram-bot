from typing import Any, Dict

from aiogram import Bot, F, Router, filters, types
from aiogram.fsm.context import FSMContext
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

from application.middlewares.administrator import AdminMiddleware
from domain.states.announcement import Announcement
from infrastructure.ioc import user_repository

router = Router()
router.message.middleware(AdminMiddleware())


@router.message(filters.Command("last_users"))
async def get_last_users(message: types.Message):
    users = await user_repository.get_last_users()
    text = "Last users:\n"
    for user in users:
        text += f"  {user['username']} - {user['last_use']}\n"
    await message.answer(text)


@router.message(filters.Command("announcement"))
async def send_post(message: types.Message, state: FSMContext):
    await state.set_state(Announcement.text)
    await message.answer(
        "Введите текст обьявления",
    )


@router.message(Announcement.text)
async def process_text(message: types.Message, state: FSMContext) -> None:
    await state.update_data(text=message.text)
    await state.set_state(Announcement.image)
    buttons = [
        [
            types.InlineKeyboardButton(text="Yes", callback_data="yes"),
            types.InlineKeyboardButton(text="No", callback_data="no"),
        ]
    ]
    await message.answer(
        f"Нужна картинка?",
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=buttons),
    )


@router.callback_query(Announcement.image, F.data.casefold() == "yes")
async def process_image_yes(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.reply(f"Отправьте картинку")


@router.callback_query(Announcement.image, F.data.casefold() == "no")
async def process_image_no(
    callback: types.CallbackQuery, state: FSMContext, bot: Bot
) -> None:
    data = await state.get_data()
    await state.clear()
    await callback.message.answer("Объявление отправлено")
    await send_announcement(data=data, bot=bot)


@router.message(Announcement.image, F.photo)
async def proccess_add_image(
    message: types.Message, state: FSMContext, bot: Bot
) -> None:
    image_from_url = message.photo[-1].file_id
    data = await state.update_data(image=image_from_url)
    await message.answer("Объявление отправлено")
    await send_announcement(data=data, bot=bot)


async def send_announcement(data: Dict[str, Any], bot: Bot) -> None:
    text = data["text"]
    image = data.get("image", "")
    users = await user_repository.get_last_users()
    if image:
        for user in users:
            await bot.send_photo(chat_id=user["id"], photo=image, caption=text)
        return
    for user in users:
        await bot.send_message(chat_id=user["id"], text=text)


@router.message(filters.Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer(
        "Cancelled.",
    )


# @router.message(filters.Command("logs"))
# async def get_logs(message: types.Message):
#     with open("log.log", "r", encoding="UTF-8") as file:
#         lines = file.readlines()
#         logs = lines[-20:]
#         text = "".join(logs)
#         await message.answer(f"logs:\n```python\n{text}\n```", parse_mode="MarkDownV2")
