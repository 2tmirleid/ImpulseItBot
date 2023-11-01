from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_btn = [[KeyboardButton(text='Panorama'), KeyboardButton(text='CapitalMS')],
          [KeyboardButton(text='Aptstore'), KeyboardButton(text='Vn1')],
          [KeyboardButton(text='Создать новый проект')]]

rpl_kb = ReplyKeyboardMarkup(keyboard=kb_btn, resize_keyboard=True, one_time_keyboard=True)
