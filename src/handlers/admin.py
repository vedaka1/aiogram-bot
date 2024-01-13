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
        await message.answer("\U00002757 <i>Permission denied</i>")


@router.message(filters.Command("logs"))
async def get_logs(message: types.Message, is_admin: bool):
    if is_admin:
        with open("log.log", 'r', encoding="UTF-8") as file:
            lines = file.readlines()
            logs = lines[-20:]
            text = "".join(logs)
            await message.answer(f'logs:\n```python\n{text}\n```', parse_mode="MarkDownV2")
    else:
        await message.answer("\U00002757 <i>Permission denied</i>")