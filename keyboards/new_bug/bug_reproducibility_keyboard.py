from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_btn = [[KeyboardButton(text='Постоянная'), KeyboardButton(text='Редкая')],
          [KeyboardButton(text='Назад')]]

rpl_kb = ReplyKeyboardMarkup(keyboard=kb_btn, resize_keyboard=True, one_time_keyboard=True)
