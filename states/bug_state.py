from aiogram.fsm.state import StatesGroup, State


class Bug(StatesGroup):
    category = State()
    platform = State()
    device = State()
    permission = State()
    site = State()
    link_on_bug_page = State()
    priority = State()
    date_of_bug = State()
    reproducibility = State()
    browser = State()
    expected_result = State()
    playback_steps = State()
    actual_result = State()
    materials = State()
    front_status = State()
    back_status = State()
    readiness = State()
    pm_comment = State()
    front_comment = State()
    back_comment = State()
    qa_comment = State()
    project_name = State()


class EditBug(StatesGroup):
    id = State()
    front_status = State()
    back_status = State()
    readiness = State()
    pm_comment = State()
    front_comment = State()
    back_comment = State()
    qa_comment = State()


class SearchBug(StatesGroup):
    id = State()
    date = State()
