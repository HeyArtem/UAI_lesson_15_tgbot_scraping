from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from aiogram import executor
from handlers import dp

'''
Главный файл, его всегда запускаю
'''


async def on_startup(dp):

    # вывод в tg bot сообщения о запуске всем админам
    await on_startup_notify(dp)

    # вывод команд с описанием
    await set_default_commands(dp)

    # выводится в терминале
    print('Бот запущен!')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
