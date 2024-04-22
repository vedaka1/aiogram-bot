import os

from aiogram import Bot, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from logic.novel import parse


async def scheduled_message(bot: Bot):
    chapters = await parse.get_last_chapters()
    last_chapter = int(chapters[0]["number"])
    last_chapter_link = chapters[0]["url"]
    if not os.path.exists(f'./translated/{last_chapter}_{"ru" or "en"}.txt'):
        await parse.get_chapter_text(last_chapter_link, last_chapter, "ru")
        file = types.FSInputFile(f"./translated/{last_chapter}_ru.txt")
        await bot.send_document(
            chat_id=426826549, document=file, caption="There is a new chapter!"
        )


def set_scheduler_tasks(scheduler: AsyncIOScheduler, bot):
    scheduler.add_job(
        scheduled_message,
        "cron",
        day_of_week="fri",
        hour="21-23",
        minute="*/30",
        second="00",
        kwargs={"bot": bot},
        id="get_last_chapter",
    )
