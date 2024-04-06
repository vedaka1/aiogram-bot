import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from application.handlers import admin, chat, images, novel
from infrastructure.ioc import init_logger
from logic.novel.shedule import set_scheduler_tasks
from settings import settings


async def main():
    init_logger()
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_routers(
        novel.router,
        admin.router,
        images.router,
        chat.router,
    )
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")  # Creating scheduler
    set_scheduler_tasks(scheduler, bot)  # Creating tasks for scheduler
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
