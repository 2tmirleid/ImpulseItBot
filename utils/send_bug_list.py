from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def send_bug_list(msg, bug):
    await msg.answer_photo(photo=f'{bug[14]}',
                           caption=f'<b>ID бага:</b> {bug[0]}\n' +
                                   f'<b>Категория бага:</b> {bug[1]}\n' +
                                   f'<b>Платформа:</b> {bug[2]}\n' +
                                   f'<b>Девайс:</b> {bug[3]}\n' +
                                   f'<b>Разрешение:</b> {bug[4]}\n' +
                                   f'<b>Сайт:</b> {bug[5]}\n' +
                                   f'<b>Ссылка на страницу бага:</b> {bug[6]}\n' +
                                   f'<b>Приоритет:</b> {bug[7]}\n' +
                                   f'<b>Дата бага:</b> {bug[8]}\n' +
                                   f'<b>Воспроизводимость:</b> {bug[9]}\n' +
                                   f'<b>Браузер:</b> {bug[10]}\n' +
                                   f'<b>Ожидаемый результат:</b> {bug[11]}\n' +
                                   f'<b>Шаги воспроизведения:</b> \n{bug[12]}\n' +
                                   f'<b>Фактический результат:</b> {bug[13]}\n' +
                                   f'<b>Статус Фронт:</b> {bug[15]}\n' +
                                   f'<b>Статус Бэк:</b> {bug[16]}\n' +
                                   f'<b>Готовность:</b> {bug[17]}\n' +
                                   f'<b>Комментарий ПМ:</b> {bug[18]}\n' +
                                   f'<b>Комментарий Фронт:</b> {bug[19]}\n' +
                                   f'<b>Комментарий Бэк:</b> {bug[20]}\n' +
                                   f'<b>Комментарий Тест:</b> {bug[21]}\n',
                           reply_markup=InlineKeyboardMarkup(
                               inline_keyboard=[[InlineKeyboardButton(text='Редактировать', callback_data=f'btn_edit-{bug[0]}')]]),
                           parse_mode='HTML')