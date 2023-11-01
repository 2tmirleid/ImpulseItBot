from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message

from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from states.project_state import Project

from keyboards import select_project_keyboard

router: Router = Router()


@router.message(CommandStart(), StateFilter(default_state))
@router.message(F.text == 'Назад')
async def get_started(msg: Message, state: FSMContext):
    await msg.answer('Выберите проект', reply_markup=select_project_keyboard.rpl_kb)
    await state.set_state(Project.name)


