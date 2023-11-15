from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def send_bug_list(msg, bug):
    await msg.answer_photo(photo=f'{bug[14]}',
                           caption=f'<b>ID бага:</b> <i>{bug[0]}</i>\n' +
                                   f'<b>Категория бага:</b> <i>{bug[1]}</i>\n' +
                                   f'<b>Платформа:</b> <i>{bug[2]}</i>\n' +
                                   f'<b>Девайс:</b> <i>{bug[3]}</i>\n' +
                                   f'<b>Разрешение:</b> <i>{bug[4]}</i>\n' +
                                   f'<b>Сайт:</b> <i>{bug[5]}</i>\n' +
                                   f'<b>Ссылка на страницу бага:</b> <i>{bug[6]}</i>\n' +
                                   f'<b>Приоритет:</b> <i>{bug[7]}</i>\n' +
                                   f'<b>Дата бага:</b> <i>{bug[8]}</i>\n' +
                                   f'<b>Воспроизводимость:</b> <i>{bug[9]}</i>\n' +
                                   f'<b>Браузер:</b> <i>{bug[10]}</i>\n' +
                                   f'<b>Ожидаемый результат:</b> <i>{bug[11]}</i>\n' +
                                   f'<b>Шаги воспроизведения:</b> \n<i>{bug[12]}</i>\n' +
                                   f'<b>Фактический результат:</b> <i>{bug[13]}</i>\n' +
                                   f'<b>Статус Фронт:</b> <i>{bug[15]}</i>\n' +
                                   f'<b>Статус Бэк:</b> <i>{bug[16]}</i>\n' +
                                   f'<b>Готовность:</b> <i>{bug[17]}</i>\n' +
                                   f'<b>Комментарий ПМ:</b> <i>{bug[18]}</i>\n' +
                                   f'<b>Комментарий Фронт:</b> <i>{bug[19]}</i>\n' +
                                   f'<b>Комментарий Бэк:</b> <i>{bug[20]}</i>\n' +
                                   f'<b>Комментарий Тест:</b> <i>{bug[21]}</i>\n',
                           reply_markup=InlineKeyboardMarkup(
                               inline_keyboard=[[InlineKeyboardButton(text='Редактировать', callback_data=f'btn_edit-{bug[0]}')],
                                                [InlineKeyboardButton(text='Удалить', callback_data=f'btn_del-{bug[0]}')]]),
                           parse_mode='HTML')