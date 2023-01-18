from aiogram import types, Dispatcher

import time
from create_bot import bot
from keyboards.keyboard import kb_client


async def cmd_start(msg: types.Message):
    await bot.send_message(msg.from_user.id, f'Здравствуйте Котичка\n\nХОТИТЕ КАТЕЙКУ??', reply_markup=kb_client)


async def send_cat(msg: types.Message):
    url = f'https://cataas.com/cat?t=${time.time()}'
    caption = 'Ваш сладенький котьек! C:'
    await bot.send_photo(msg.chat.id, photo=url, caption=caption, reply_markup=kb_client)


async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'ХОТИТЕ КАТЕЙКУ??', reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):

    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(send_cat, text='ХОЧУ КАТЕЙКУ <3')
    dp.register_message_handler(echo_message)
