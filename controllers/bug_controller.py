import psycopg2
from postgresql.connection_settings import conn

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards import backspace_keyboard

cursor: conn = conn.cursor()


async def add_task(msg, category, platform, device,
                   permission, site, link_on_bug_page, priority,
                   date_of_bug, reproducibility, browser, expected_result,
                   playback_steps, actual_result, materials, front_status, back_status,
                   readiness, pm_comment, front_comment, back_comment, qa_comment, project_name):
    global cursor
    try:
        cursor.execute(
            f"""INSERT INTO {project_name.lower()} (category, platform, device,
                                      permission, site, link_on_bug_page, priority,
                                      date_of_bug, reproducibility, browser, expected_result,
                                      playback_steps, actual_result, materials, front_status, back_status,
                                      readiness, pm_comment, front_comment, back_comment, qa_comment, project_name) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (category, platform, device,
             permission, site, link_on_bug_page, priority,
             date_of_bug, reproducibility, browser, expected_result,
             playback_steps, actual_result, materials, front_status, back_status,
             readiness, pm_comment, front_comment, back_comment, qa_comment, project_name)
        )
        conn.commit()
        await msg.answer('Баг-лист успешно создан')

    except psycopg2.errors.UniqueViolation as err:
        await msg.answer('Упс, похоже, что при создании возникла какая-то ошибка')
        print(err)


async def get_all_bug_lists(msg, project_name):
    global cursor
    try:
        cursor.execute(
            f"""SELECT * FROM {project_name}"""
        )

        tasks = cursor.fetchall()
        for task in tasks:
            await msg.answer_photo(photo=f'{task[14]}',
                                   caption=f'<b>ID бага:</b> {task[0]}\n' +
                                           f'<b>Категория бага:</b> {task[1]}\n' +
                                           f'<b>Платформа:</b> {task[2]}\n' +
                                           f'<b>Девайс:</b> {task[3]}\n' +
                                           f'<b>Разрешение:</b> {task[4]}\n' +
                                           f'<b>Сайт:</b> {task[5]}\n' +
                                           f'<b>Ссылка на страницу бага:</b> {task[6]}\n' +
                                           f'<b>Приоритет:</b> {task[7]}\n' +
                                           f'<b>Дата бага:</b> {task[8]}\n' +
                                           f'<b>Воспроизводимость:</b> {task[9]}\n' +
                                           f'<b>Браузер:</b> {task[10]}\n' +
                                           f'<b>Ожидаемый результат:</b> {task[11]}\n' +
                                           f'<b>Шаги воспроизведения:</b> \n{task[12]}\n' +
                                           f'<b>Фактический результат:</b> {task[13]}\n' +
                                           f'<b>Статус Фронт:</b> {task[15]}\n' +
                                           f'<b>Статус Бэк:</b> {task[16]}\n' +
                                           f'<b>Готовность:</b> {task[17]}\n' +
                                           f'<b>Комментарий ПМ:</b> {task[18]}\n' +
                                           f'<b>Комментарий Фронт:</b> {task[19]}\n' +
                                           f'<b>Комментарий Бэк:</b> {task[20]}\n' +
                                           f'<b>Комментарий Тест:</b> {task[21]}\n',
                                   reply_markup=InlineKeyboardMarkup(
                                       inline_keyboard=[[InlineKeyboardButton(text='Редактировать', callback_data=f'btn_edit-{task[0]}')]]),
                                   parse_mode='HTML')

    except psycopg2.errors.UniqueViolation as err:
        await msg.answer('Упс, похоже, что при просмотре возникла какая-то ошибка')
        print(err)


async def edit_task(msg, bug_id, project_name, front_status, back_status, readiness,
                    pm_comment, front_comment, back_comment, qa_comment):
    global cursor
    try:
        cursor.execute(
            f"""UPDATE {project_name} SET front_status = '{front_status}', back_status = '{back_status}',
             readiness = '{readiness}', pm_comment = '{pm_comment}', front_comment = '{front_comment}',
             back_comment = '{back_comment}', qa_comment = '{qa_comment}' WHERE id = '{bug_id}'"""
        )
        conn.commit()
        await msg.answer('Редактирование прошло успешно', reply_markup=backspace_keyboard.rpl_kb)

    except psycopg2.errors.UniqueViolation as err:
        await msg.answer('Упс, похоже, что при просмотре возникла какая-то ошибка')
        print(err)
