from aiogram.fsm.state import State, StatesGroup


class Announcement(StatesGroup):
    text = State()
    image = State()
