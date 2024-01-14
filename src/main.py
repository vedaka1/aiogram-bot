import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from resources import parse, config
from resources.database import Database
from handlers import novel, chat, admin


db = Database()


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(
        novel.router,
        admin.router,
        chat.router
    )
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow') # Creating scheduler
    set_scheduler_tasks(scheduler, bot) # Creating tasks for scheduler
    scheduler.start()
    await dp.start_polling(bot)


async def sheduled_message(bot: Bot, scheduler: AsyncIOScheduler):
    chapters = parse.get_last_chapters()
    last_chapter = int(chapters[0][0])
    last_chapter_link = chapters[0][1]
    if not os.path.exists(f'./translated/{last_chapter}_{"ru" or "en"}.txt'):
        parse.get_chapter_text(last_chapter_link, last_chapter, 'ru')
        file = types.FSInputFile(f'./translated/{last_chapter}_ru.txt')
        await bot.send_document(
            chat_id=426826549,
            document=file,
            caption='There is a new chapter!'
        )


def set_scheduler_tasks(scheduler: AsyncIOScheduler, bot):
    scheduler.add_job(
        sheduled_message,
        'cron',
        day_of_week ='fri',
        hour='21-23',
        minute='*/30',
        second='00',
        kwargs={'bot': bot, 'scheduler': scheduler},
        id='get_last_chapter'
    )


if __name__ == "__main__":
    # filename='log.log',
    logging.basicConfig(
        filename='log.log',
        level=logging.INFO,
        encoding='UTF-8',
        format='%(asctime)s %(levelname)s: %(message)s'
    )
    logger = logging.getLogger()
    asyncio.run(main())
