from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.project_state import Project
from states.bug_state import Bug, EditBug

from controllers import bug_controller

from routers import start_router

from keyboards import select_project_action_keyboard, select_all_or_date_of_bug_list_keyboard, backspace_keyboard
from keyboards.new_bug import bug_category_keyboard, bug_front_status_keyboard


router: Router = Router()


@router.message(StateFilter(Project.name), F.text)
async def get_project_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('Выберите действие', reply_markup=select_project_action_keyboard.rpl_kb)
    await state.set_state(Project.action)


@router.message(StateFilter(Project.action), F.text)
async def get_project_action(msg: Message, state: FSMContext):
    await state.update_data(action=msg.text)
    data = await state.get_data()
    action = data.get('action')
    name = data.get('name')

    if action == 'Создать баг-лист':
        await msg.answer('Выберите категорию бага', reply_markup=bug_category_keyboard.rpl_kb)
        await state.set_state(Bug.category)
    elif action == 'Посмотреть баг-лист':
        await msg.answer('Выберите действие', reply_markup=select_all_or_date_of_bug_list_keyboard.rpl_kb)
        await state.set_state(Project.all_or_date)


@router.message(StateFilter(Project.all_or_date), F.text)
async def get_project_data(msg: Message, state: FSMContext):
    await state.update_data(all_or_date=msg.text)
    data = await state.get_data()
    all_or_date = data.get('all_or_date')
    name = data.get('name')

    if all_or_date == 'Смотреть все баг-листы':
        await bug_controller.get_all_bug_lists(msg, name)
        await msg.answer('Чтобы вернуться назад, нажмите кнопку "Назад"', reply_markup=backspace_keyboard.rpl_kb)
        # await state.clear()


@router.callback_query(lambda query: query.data.startswith('btn_edit'))
async def edit_task(clb_query: types.CallbackQuery, state: FSMContext):
    bug_id = clb_query.data[-1]
    await state.set_state(EditBug.id)
    await state.update_data(id=bug_id)
    await clb_query.message.answer('Выберите фронт статус', reply_markup=bug_front_status_keyboard.rpl_kb)
    await state.set_state(EditBug.front_status)


# @router.message(F.text == 'Назад')
# async def get_back(msg: Message, state: FSMContext):
#     await start_router.get_started(msg, state)
#     #await state.clear()

