from aiogram import types

'''
описания команд (контекст) прописанных в users, 
описания выводятся даже если для них нет скрипта в users
'''


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('menu', 'Вызов стартовой страницы'),
        types.BotCommand('fsmt', 'протестить работу моего fsm (3 вопроса)'),
        # types.BotCommand('Привет', 'Здоровается, упоминает имя')
    ])
