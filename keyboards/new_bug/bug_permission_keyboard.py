from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_btn = [[KeyboardButton(text='x360'), KeyboardButton(text='x768')],
          [KeyboardButton(text='x1024'), KeyboardButton(text='x1920')],
          [KeyboardButton(text='>x1920'), KeyboardButton(text='Все')],
          [KeyboardButton(text='Назад')]]

rpl_kb = ReplyKeyboardMarkup(keyboard=kb_btn, resize_keyboard=True, one_time_keyboard=True)
