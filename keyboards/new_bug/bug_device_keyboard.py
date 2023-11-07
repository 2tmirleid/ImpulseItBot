from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_btn = [[KeyboardButton(text='Десктоп'), KeyboardButton(text='Телефон')],
          [KeyboardButton(text='Планшет'), KeyboardButton(text='Все')],
          [KeyboardButton(text='Назад')]]

rpl_kb = ReplyKeyboardMarkup(keyboard=kb_btn, resize_keyboard=True, one_time_keyboard=True)
