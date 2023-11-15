import io

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from openpyxl import Workbook

from controllers import bug_controller

router: Router = Router()


@router.message(F.text == 'export')
async def export_to_excel(msg: Message, state: FSMContext):
    await msg.answer('work')
    data = await state.get_data()
    project_name = data.get('name')

    bugs = await bug_controller.export_to_excel(msg, project_name)

    wb = Workbook
    ws = wb.active

    for bug in bugs:
        ws.append(bug)

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    with open("data.xlsx", "wb") as file:
        file.write(buffer.read())
