from aiogram.fsm.state import State, StatesGroup


class Project(StatesGroup):
    name = State()
    action = State()
    all_or_date = State()


class NewProject(StatesGroup):
    new_name = State()

