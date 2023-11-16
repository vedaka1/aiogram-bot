from aiogram import Router, types, filters
from resources.database import Database
from middlewares.administrator import AdminMiddleware


router = Router()
db = Database()
router.message.middleware(AdminMiddleware())

@router.message(filters.Command("last_users"))
async def get_last_users(message: types.Message, is_admin: bool):
    if is_admin:
        users = db.get_last_users()
        text = f"Last users:\n"
        for user in users:
            text += f"  {user['username']} - {user['last_use']}\n"
        await message.answer(text)
    else:
        await message.answer("_Permission denided_")