import psycopg2
from postgresql.connection_settings import conn

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards import backspace_keyboard

from utils import send_bug_list

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
            f"""SELECT * FROM {project_name.lower()}"""
        )

        bugs = cursor.fetchall()
        for bug in bugs:
            await send_bug_list.send_bug_list(msg, bug)

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


async def delete_bug_by_id(msg, bug_id, project_name):
    global cursor
    try:
        cursor.execute(
            f"""DELETE FROM {project_name} WHERE id = {bug_id}"""
        )
        conn.commit()
    except psycopg2.errors.UniqueViolation as err:
        print(err)


async def get_bug_lists_by_date(msg, project_name, date_of_bug):
    global cursor
    try:
        cursor.execute(
            f"""SELECT * FROM {project_name.lower()} WHERE date_of_bug = '{date_of_bug}'"""
        )
        bugs = cursor.fetchall()

        for bug in bugs:
            await send_bug_list.send_bug_list(msg, bug)
            await msg.answer('Чтобы вернуться назад, нажмите кнопку "Назад"', reply_markup=backspace_keyboard.rpl_kb)
    except psycopg2.errors.UniqueViolation as err:
        await msg.answer('Упс, похоже, что при просмотре возникла какая-то ошибка')
        print(err)


async def export_to_excel(msg, project_name):
    global cursor
    try:
        cursor.execute(
            f"""SELECT * FROM тест"""
        )
        bugs = cursor.fetchall()
        return bugs
    except psycopg2.errors.UniqueViolation as err:
        await msg.answer('Упс, похоже, что при просмотре возникла какая-то ошибка')
        print(err)