from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.bug_state import Bug, EditBug

from controllers import bug_controller

from keyboards.new_bug import bug_platform_keyboard, bug_device_keyboard, bug_permission_keyboard, \
    bug_reproducibility_keyboard, bug_browser_keyboard, bug_front_status_keyboard, bug_back_status_keyboard, \
    bug_readiness_keyboard

from keyboards import backspace_keyboard

router: Router = Router()


@router.message(StateFilter(Bug.category), F.text)
async def get_new_bug_platform(msg: Message, state: FSMContext):
    await state.update_data(category=msg.text)
    await msg.answer('Выберите платформу, на которой был замечен баг', reply_markup=bug_platform_keyboard.rpl_kb)
    await state.set_state(Bug.platform)


@router.message(StateFilter(Bug.platform), F.text)
async def get_new_bug_device(msg: Message, state: FSMContext):
    await state.update_data(platform=msg.text)
    await msg.answer('Выберите девайс, на котором был замечен баг', reply_markup=bug_device_keyboard.rpl_kb)
    await state.set_state(Bug.device)


@router.message(StateFilter(Bug.device), F.text)
async def get_new_bug_permission(msg: Message, state: FSMContext):
    await state.update_data(device=msg.text)
    await msg.answer('Выберите разрешение, на котором был замечен баг', reply_markup=bug_permission_keyboard.rpl_kb)
    await state.set_state(Bug.permission)


@router.message(StateFilter(Bug.permission), F.text)
async def get_new_bug_site(msg: Message, state: FSMContext):
    await state.update_data(permission=msg.text)
    await msg.answer('Введите сайт, на котором был замечен баг')
    await state.set_state(Bug.site)


@router.message(StateFilter(Bug.site), F.text)
async def get_new_bug_page_link(msg: Message, state: FSMContext):
    await state.update_data(site=msg.text)
    await msg.answer('Введите ссылку на страницу бага, на которой был замечен баг')
    await state.set_state(Bug.link_on_bug_page)


@router.message(StateFilter(Bug.link_on_bug_page), F.text)
async def get_new_bug_priority(msg: Message, state: FSMContext):
    await state.update_data(link_on_bug_page=msg.text)
    await msg.answer('Введите приоритет бага')
    await state.set_state(Bug.priority)


@router.message(StateFilter(Bug.priority), F.text)
async def get_new_bug_date(msg: Message, state: FSMContext):
    await state.update_data(priority=msg.text)
    await msg.answer('Введите дату обнаружения бага')
    await state.set_state(Bug.date_of_bug)


@router.message(StateFilter(Bug.date_of_bug), F.text)
async def get_new_bug_reproducibility(msg: Message, state: FSMContext):
    await state.update_data(date_of_bug=msg.text)
    await msg.answer('Выберите воспроизводимость бага', reply_markup=bug_reproducibility_keyboard.rpl_kb)
    await state.set_state(Bug.reproducibility)


@router.message(StateFilter(Bug.reproducibility), F.text)
async def get_new_bug_browser(msg: Message, state: FSMContext):
    await state.update_data(reproducibility=msg.text)
    await msg.answer('Выберите браузер, в котором был замечен баг', reply_markup=bug_browser_keyboard.rpl_kb)
    await state.set_state(Bug.browser)


@router.message(StateFilter(Bug.browser), F.text)
async def get_new_bug_expected_result(msg: Message, state: FSMContext):
    await state.update_data(browser=msg.text)
    await msg.answer('Введите ожидаемый результат')
    await state.set_state(Bug.expected_result)


@router.message(StateFilter(Bug.expected_result), F.text)
async def get_new_bug_playback_steps(msg: Message, state: FSMContext):
    await state.update_data(expected_result=msg.text)
    await msg.answer('Введите шаги воспроизведения бага')
    await state.set_state(Bug.playback_steps)


@router.message(StateFilter(Bug.playback_steps), F.text)
async def get_new_bug_actual_result(msg: Message, state: FSMContext):
    await state.update_data(playback_steps=msg.text)
    await msg.answer('Введите фактический результат')
    await state.set_state(Bug.actual_result)


@router.message(StateFilter(Bug.actual_result), F.text)
async def get_new_bug_materials(msg: Message, state: FSMContext):
    await state.update_data(actual_result=msg.text)
    await msg.answer('Вставьте ссылку на фото бага')
    await state.set_state(Bug.materials)


@router.message(StateFilter(Bug.materials), F.text)
async def get_new_bug_front_status(msg: Message, state: FSMContext):
    await state.update_data(materials=msg.text)
    await msg.answer('Выберите фронт статус', reply_markup=bug_front_status_keyboard.rpl_kb)
    await state.set_state(Bug.front_status)


@router.message(StateFilter(Bug.front_status), F.text)
async def get_new_bug_back_status(msg: Message, state: FSMContext):
    await state.update_data(front_status=msg.text)
    await msg.answer('Выберите бэк статус', reply_markup=bug_back_status_keyboard.rpl_kb)
    await state.set_state(Bug.back_status)


@router.message(StateFilter(Bug.back_status), F.text)
async def get_new_bug_readiness(msg: Message, state: FSMContext):
    await state.update_data(back_status=msg.text)
    await msg.answer('Выберите готовность', reply_markup=bug_readiness_keyboard.rpl_kb)
    await state.set_state(Bug.readiness)


@router.message(StateFilter(Bug.readiness), F.text)
async def get_new_bug_pm_comment(msg: Message, state: FSMContext):
    await state.update_data(readiness=msg.text)
    await msg.answer('Введите комментарий ПМ\'а')
    await state.set_state(Bug.pm_comment)


@router.message(StateFilter(Bug.pm_comment), F.text)
async def get_new_bug_front_comment(msg: Message, state: FSMContext):
    await state.update_data(pm_comment=msg.text)
    await msg.answer('Введите комментарий фронта')
    await state.set_state(Bug.front_comment)


@router.message(StateFilter(Bug.front_comment), F.text)
async def get_new_bug_back_comment(msg: Message, state: FSMContext):
    await state.update_data(front_comment=msg.text)
    await msg.answer('Введите комментарий бэка')
    await state.set_state(Bug.back_comment)


@router.message(StateFilter(Bug.back_comment), F.text)
async def get_new_bug_qa_comment(msg: Message, state: FSMContext):
    await state.update_data(back_comment=msg.text)
    await msg.answer('Введите комментарий тестера')
    await state.set_state(Bug.qa_comment)


@router.message(StateFilter(Bug.qa_comment), F.text)
async def get_new_bug_project_name(msg: Message, state: FSMContext):
    await state.update_data(qa_comment=msg.text)
    await msg.answer('Введите название проекта')
    await state.set_state(Bug.project_name)


@router.message(StateFilter(Bug.project_name), F.text)
async def get_new_bug_data(msg: Message, state: FSMContext):
    await state.update_data(project_name=msg.text)
    data = await state.get_data()

    category = data.get('category')
    platform = data.get('platform')
    device = data.get('device')
    permission = data.get('permission')
    site = data.get('site')
    link_on_bug_page = data.get('link_on_bug_page')
    priority = data.get('priority')
    date_of_bug = data.get('date_of_bug')
    reproducibility = data.get('reproducibility')
    browser = data.get('browser')
    expected_result = data.get('expected_result')
    playback_steps = data.get('playback_steps')
    actual_result = data.get('actual_result')
    materials = data.get('materials')
    front_status = data.get('front_status')
    back_status = data.get('back_status')
    readiness = data.get('readiness')
    pm_comment = data.get('pm_comment')
    front_comment = data.get('front_comment')
    back_comment = data.get('back_comment')
    qa_comment = data.get('qa_comment')
    project_name = data.get('project_name')

    await bug_controller.add_task(msg, category, platform, device,
                                  permission, site, link_on_bug_page, priority,
                                  date_of_bug, reproducibility, browser, expected_result,
                                  playback_steps, actual_result, materials, front_status, back_status,
                                  readiness, pm_comment, front_comment, back_comment, qa_comment, project_name)



    await msg.answer('Чтобы вернуться назад, нажмите кнопку "Назад"', reply_markup=backspace_keyboard.rpl_kb)
    # await state.clear()

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
