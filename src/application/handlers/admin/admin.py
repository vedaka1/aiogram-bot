from aiogram import Router, filters, types

from application.handlers.admin.commands import announcement
from application.middlewares.administrator import AdminMiddleware
from infrastructure.ioc import user_repository

router = Router()
router.include_router(announcement.announcement_router)
router.message.middleware(AdminMiddleware())


@router.message(filters.Command("last_users"))
async def get_last_users(message: types.Message):
    users = await user_repository.get_last_users()
    text = "Last users:\n"
    for user in users:
        text += f"  {user['username']} - {user['last_use']}\n"
    await message.answer(text)


# @router.message(filters.Command("logs"))
# async def get_logs(message: types.Message):
#     with open("log.log", "r", encoding="UTF-8") as file:
#         lines = file.readlines()
#         logs = lines[-20:]
#         text = "".join(logs)
#         await message.answer(f"logs:\n```python\n{text}\n```", parse_mode="MarkDownV2")
