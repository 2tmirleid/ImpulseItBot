from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from controllers import project_controller


async def select_project_keyboard():
    projects = project_controller.get_all_projects()
    buttons = [KeyboardButton(text=project) for project in reversed(projects)]

    if len(buttons) % 2 != 0:
        buttons.append(KeyboardButton(text=''))

    keyboard = [*zip(*[iter(buttons)] * 2)]

    rpl_kb = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return rpl_kb
