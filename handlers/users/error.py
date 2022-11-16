from aiogram import types
from loader import dp

'''
Обработчик несуществующих команд
ответ на любую команду "Такой команды нет"
'''


@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f'Команда  "{message.text}" не найдена.')    
