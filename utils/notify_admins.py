import logging
from aiogram import Dispatcher
from data.config import admins

'''
Скрипт проходит в цикле по id админов
(берет их из config.py)
отправляет в tg bot сообщение о запуске бота

'''

async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text = 'Бот запущен!\nтеперь нужно кликнуть Menu и выбрать "/start"\nили просто кликнуть\n\n /start'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err) 
