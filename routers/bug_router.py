from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.bug_state import Bug, EditBug, SearchBug

from controllers import bug_controller

from keyboards.new_bug import bug_platform_keyboard, bug_device_keyboard, bug_permission_keyboard, \
    bug_reproducibility_keyboard, bug_browser_keyboard, bug_front_status_keyboard, bug_back_status_keyboard, \
    bug_readiness_keyboard, bug_category_keyboard

from keyboards import backspace_keyboard, select_all_or_date_of_bug_list_keyboard
from states.project_state import Project

router: Router = Router()


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
    elif all_or_date == 'Посмотреть баг-лист по дате':
        await msg.answer('Введите дату создания баг-листа в формате дд.мм.гггг')
        await state.set_state(SearchBug.date)


@router.callback_query(lambda query: query.data.startswith('btn_edit'))
async def edit_task(clb_query: types.CallbackQuery, state: FSMContext):
    bug_id = clb_query.data[-1]
    await state.set_state(EditBug.id)
    await state.update_data(id=bug_id)
    await clb_query.message.answer('Выберите фронт статус', reply_markup=bug_front_status_keyboard.rpl_kb)
    await state.set_state(EditBug.front_status)


@router.message(StateFilter(SearchBug.date), F.text)
async def get_bug_list_by_date(msg: Message, state: FSMContext):
    await state.update_data(date=msg.text)
    data = await state.get_data()
    date = data.get('date')
    project_name = data.get('name')

    await bug_controller.get_bug_lists_by_date(msg, project_name, date)
