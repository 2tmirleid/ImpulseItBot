from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_btn = [[KeyboardButton(text='Google chrome'), KeyboardButton(text='Yandex browser')],
          [KeyboardButton(text='Edge'), KeyboardButton(text='Mozilla')],
          [KeyboardButton(text='Opera'), KeyboardButton(text='Safari')],
          [KeyboardButton(text='Все')]]

rpl_kb = ReplyKeyboardMarkup(keyboard=kb_btn, resize_keyboard=True, one_time_keyboard=True)
