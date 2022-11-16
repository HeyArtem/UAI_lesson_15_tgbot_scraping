from aiogram import types
from loader import dp

'''
ответ на команду Привет
'''


@dp.message_handler(text='Привет')
async def command_hello(message: types.Message):
    await message.reply(f'Привет {message.from_user.full_name}!')
