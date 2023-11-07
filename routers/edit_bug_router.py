from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from controllers import bug_controller
from keyboards.new_bug import bug_back_status_keyboard, bug_readiness_keyboard
from states.bug_state import EditBug

router: Router = Router()


@router.message(StateFilter(EditBug.front_status), F.text)
async def get_bug_edit_front_status(msg: Message, state: FSMContext):
    await state.update_data(front_status=msg.text)
    await msg.answer('Выберите бэк статус', reply_markup=bug_back_status_keyboard.rpl_kb)
    await state.set_state(EditBug.back_status)


@router.message(StateFilter(EditBug.back_status), F.text)
async def get_bug_edit_back_status(msg: Message, state: FSMContext):
    await state.update_data(back_status=msg.text)
    await msg.answer('Выберите готовность', reply_markup=bug_readiness_keyboard.rpl_kb)
    await state.set_state(EditBug.readiness)


@router.message(StateFilter(EditBug.readiness), F.text)
async def get_bug_edit_readiness(msg: Message, state: FSMContext):
    await state.update_data(readiness=msg.text)
    await msg.answer('Введите комментарий ПМ\'а')
    await state.set_state(EditBug.pm_comment)


@router.message(StateFilter(EditBug.pm_comment), F.text)
async def get_bug_edit_pm_comment(msg: Message, state: FSMContext):
    await state.update_data(pm_comment=msg.text)
    await msg.answer('Введите комментарий фронт')
    await state.set_state(EditBug.front_comment)


@router.message(StateFilter(EditBug.front_comment), F.text)
async def get_bug_edit_front_comment(msg: Message, state: FSMContext):
    await state.update_data(front_comment=msg.text)
    await msg.answer('Введите комментарий бэк')
    await state.set_state(EditBug.back_comment)


@router.message(StateFilter(EditBug.back_comment), F.text)
async def get_bug_edit_back_comment(msg: Message, state: FSMContext):
    await state.update_data(back_comment=msg.text)
    await msg.answer('Введите комментарий тест')
    await state.set_state(EditBug.qa_comment)


@router.message(StateFilter(EditBug.qa_comment), F.text)
async def get_bug_edit_data(msg: Message, state: FSMContext):
    await state.update_data(qa_comment=msg.text)
    data = await state.get_data()

    project_name = data.get('name')

    bug_id = data.get('id')
    front_status = data.get('front_status')
    back_status = data.get('back_status')
    readiness = data.get('readiness')
    pm_comment = data.get('pm_comment')
    front_comment = data.get('front_comment')
    back_comment = data.get('back_comment')
    qa_comment = data.get('qa_comment')

    await bug_controller.edit_task(msg, bug_id, project_name, front_status, back_status, readiness, pm_comment,
                                   front_comment, back_comment, qa_comment)
