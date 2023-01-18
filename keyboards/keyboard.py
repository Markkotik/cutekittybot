from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton('ХОЧУ КАТЕЙКУ <3')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(button1)
