from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from controllers import bug_controller

from keyboards import backspace_keyboard

router: Router = Router()


@router.callback_query(lambda query: query.data.startswith('btn_del'))
async def delete_task(clb_query: types.CallbackQuery, state: FSMContext):
    bug_id = clb_query.data[-1]
    data = await state.get_data()
    project_name = data.get('name')

    await bug_controller.delete_bug_by_id(Message, bug_id, project_name)
    await clb_query.message.answer('Удаление успешно, чтобы вернуться назад, нажмите кнопку назад',
                                   reply_markup=backspace_keyboard.rpl_kb)
