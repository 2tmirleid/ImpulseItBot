from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_btn = [[KeyboardButton(text='Новое'), KeyboardButton(text='Взято в работу')],
          [KeyboardButton(text='Уточнение'), KeyboardButton(text='Исправлено')],
          [KeyboardButton(text='Проверено (коммит)'), KeyboardButton(text='Пропущено')],
          [KeyboardButton(text='Ожидание верстки'), KeyboardButton(text='Назад')]]

rpl_kb = ReplyKeyboardMarkup(keyboard=kb_btn, resize_keyboard=True, one_time_keyboard=True)
