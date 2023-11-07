from postgresql.connection_settings import conn
import psycopg2
from aiogram.fsm.context import FSMContext

from keyboards import backspace_keyboard

from routers import start_router

cursor: conn = conn.cursor()


async def create_project(msg, project_name, state: FSMContext):
    global cursor
    try:
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {project_name.lower()} 
            (id SERIAL PRIMARY KEY,
             category varchar,
             platform varchar,
             device varchar,
             permission varchar,
             site varchar,
             link_on_bug_page varchar,
             priority varchar,
             date_of_bug varchar,
             reproducibility varchar,
             browser varchar,
             expected_result varchar,
             playback_steps varchar,
             actual_result varchar,
             materials varchar,
             front_status varchar,
             back_status varchar,
             readiness varchar,
             pm_comment varchar,
             front_comment varchar,
             back_comment varchar,
             qa_comment varchar,
             project_name varchar)"""
        )
        conn.commit()
        cursor.execute(
            f"""INSERT INTO project_names_for_keyboard (name) VALUES (%s)""",
            (project_name,)
        )
        conn.commit()
        await msg.answer(f'Создание проекта {project_name} завершено успешно')
        # await msg.answer('Чтобы вернуться назад, нажмите кнопку "Назад"', reply_markup=backspace_keyboard.rpl_kb)
        await start_router.get_started(msg, state)

    except psycopg2.errors.UniqueViolation as err:
        await msg.answer('Упс, похоже, что при просмотре возникла какая-то ошибка')
        print(err)


def get_all_projects():
    global cursor
    try:
        cursor.execute(
            f"""SELECT * FROM project_names_for_keyboard"""
        )
        projects = cursor.fetchall()
        return [project[1] for project in projects]
    except psycopg2.errors.UniqueViolation as err:
        print(err)


# def is_project_deleted(project_name):
#     global cursor
#     try:
#         cursor.execute(
#             f"""SELECT * FROM {project_name.lower()}"""
#         )
#         project = cursor.fetchone()
#         if project:
#             return False
#         else:
#             return True
#     except psycopg2.errors.UniqueViolation as err:
#         print(err)
