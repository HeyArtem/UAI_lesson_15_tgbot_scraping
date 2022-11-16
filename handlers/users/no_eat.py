from aiogram import types
from loader import dp
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import text, bold, italic
from aiogram.types import ParseMode
import time
from keyboards.inline.inline_kb import(
    ikb_no_eat
    )
from keyboards.default import first_kb
from .dixy import dixy_data
import json
from states import TestFsm  # my class


'''
Все Хэндлеры (Инлайн) не свзяанные с веткой еды 
'''


@dp.message_handler(text='Нет, тот раздел меня уже не интересует!')
async def no_eat(message: types.Message):        
    await message.answer(text='🪐 Инлайн раздел', reply_markup=ikb_no_eat)


@dp.callback_query_handler(text='Заглушка')
async def plug(call: CallbackQuery):
    await call.answer('👨🏼‍💻 Это ответ на заглушка', show_alert=True)


@dp.callback_query_handler(text='fsmt')
async def my_fsm1(call: CallbackQuery):
    
    # удаляю клавиатуру 
    await call.message.answer(text='Начинаем тестировать мою fsm,\nТвое имя?', reply_markup=types.ReplyKeyboardRemove())
    
    
    
    # открыл на запись FSM, продолжение в fsmtest.py
    await TestFsm.test1.set()
    

@dp.callback_query_handler(text='Scraping')
async def sraping_dixy(call: CallbackQuery):    
    
    # активирую функцию сбора данных
    dixy_data()

    # сообщения для вывода
    msg = text(bold('Активирована функция сбора данных Dixy \nЗдесь я применил новый метод bold'))
    msg2 = text(italic('...сейчас выведется результат первой страницы \nЗдесь я применил новый метод italic.'))
    msg3 = text(bold('Сбор данных закончен!'))

    # отправляю сообщения с паузами, тяну время, что бы функция отработала
    await call.message.answer(msg, parse_mode=ParseMode.MARKDOWN)
    time.sleep(1)
    await call.message.answer(msg2, parse_mode=ParseMode.MARKDOWN)
    time.sleep(2)

    # читаю сохраненный json
    with open('dixy_data/all_data_dixy.json') as file:
        data = file.read()
        json_data = json.loads(data)
    res = json.dumps(json_data, indent=4, ensure_ascii=False)

    # вывожу результаты в мессенджер
    await call.message.answer(res)

    await call.message.answer(msg3, parse_mode=ParseMode.MARKDOWN, reply_markup=ikb_no_eat)
    await call.answer()


@dp.callback_query_handler(text='menu')
async def no_eat(call: CallbackQuery):        
    await call.message.answer(text='Привет, желаешь сделать заказ еды?', reply_markup=first_kb)
    await call.answer()
