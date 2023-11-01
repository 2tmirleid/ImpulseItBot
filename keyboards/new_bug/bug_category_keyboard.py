from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_btn = [[KeyboardButton(text='Верстка'), KeyboardButton(text='Функциональность')],
          [KeyboardButton(text='Валидация'), KeyboardButton(text='Кликабельность')]]

rpl_kb = ReplyKeyboardMarkup(keyboard=kb_btn, resize_keyboard=True, one_time_keyboard=True)
