import asyncio, logging
from aiogram import Bot, Dispatcher, types
from resources import parse, config
from resources.database import Database
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers import novel, chat


db = Database()


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(chat.router, novel.router)

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    set_scheduler_tasks(scheduler, bot) # Creating tasks for scheduler
    scheduler.start()

    await dp.start_polling(bot)


async def shedule_message(bot):
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
    await bot.send_message(chat_id=426826549, text="<a href='https://readlightnovel.app/the-beginning-after-the-end-535558'>The Beginning After The End</a>\nThere is a new chapter!\nChoose chapter to translate:", reply_markup=keyboard)


def set_scheduler_tasks(scheduler: AsyncIOScheduler, bot):
    scheduler.add_job(shedule_message, 'cron', day_of_week ='fri', hour='21', minute='00', second='00', kwargs={'bot': bot})


if __name__ == "__main__":
    logging.basicConfig(filename='log_file.log',
                        level=logging.INFO,
                        encoding='UTF-8',
                        format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger()
    asyncio.run(main())