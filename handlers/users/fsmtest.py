from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.dispatcher.filters import Command
from states import TestFsm  # my class
from keyboards.inline.inline_kb import ikb_no_eat

'''
Мини тест-опрос для FSM

Задам три вопроса:
-Твое имя
-Любимая модель авто
-Любимая сторона света
'''


@dp.message_handler(Command('fsmt'))
async def my_fsm1(message: types.Message):
    await message.answer('Начинаем тестировать мою fsm,\nТвое имя?')
    await TestFsm.test1.set()


@dp.message_handler(state=TestFsm.test1)
async def my_state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)

    await message.answer('Любимая модель авто') #где то был replay
    await TestFsm.test2.set()


@dp.message_handler(state=TestFsm.test2)
async def my_state2(message: types.Message, state: FSMContext):
    answer2 = message.text

    await state.update_data(test2=answer2)

    await message.answer('Любимая сторона света')
    await TestFsm.test3.set()


@dp.message_handler(state=TestFsm.test3)
async def my_state3(message: types.Message, state: FSMContext):
    answer3 = message.text

    await state.update_data(test3=answer3)

    # достаю данные для ответа
    data = await state.get_data()
    name = data.get('test1')
    avto = data.get('test2')
    sideWorld = data.get('test3')

    await message.answer(
        f'Тест пройден\n'
        f'Твое имя: {name}\n'
        f'Любимое авто: {avto}\n'
        f'Любимая сторона света: {sideWorld}\n'
    )

    await state.finish()
    await message.answer('👽 Пока вроде работает ',reply_markup=ikb_no_eat)
