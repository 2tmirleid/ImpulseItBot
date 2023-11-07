from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.project_state import Project, NewProject
from states.bug_state import Bug, EditBug, SearchBug

from controllers import bug_controller, project_controller

from routers import start_router

from keyboards import select_project_action_keyboard, select_all_or_date_of_bug_list_keyboard, backspace_keyboard
from keyboards.new_bug import bug_category_keyboard, bug_front_status_keyboard

router: Router = Router()


@router.message(StateFilter(Project.name), F.text)
async def get_project_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    data = await state.get_data()
    name = data.get('name')
    if name == 'Создать новый проект':
        await msg.answer('Введите название проекта')
        await state.set_state(NewProject.new_name)
    else:
        await msg.answer('Выберите действие', reply_markup=select_project_action_keyboard.rpl_kb)
        await state.set_state(Project.action)


@router.message(StateFilter(NewProject.new_name), F.text)
async def get_new_project_name(msg: Message, state: FSMContext):
    await state.update_data(new_name=msg.text)
    data = await state.get_data()
    name = data.get('new_name')
    await project_controller.create_project(msg, name, state)


