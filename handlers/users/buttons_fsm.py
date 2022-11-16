from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from keyboards.default import (drink_kb, first_kb, main_kb,
                               pizza_kb_fish_staffing, 
                               pizza_kb_fruit_staffing,
                               pizza_kb_kind, 
                               pizza_kb_meat_staffing,
                               pizza_kb_size
                               )
from keyboards.inline import yes_or_no_kb
from loader import dp
from states import MenuFsm  # my class


'''
Хэндлеры от обычных кнопок (без инлайн клавиатыры), раздел Пицца 
ловят ответы пользователя состояния записываю в fsm
'''


# Приветствие
@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(
        f'Привет {message.from_user.full_name}! \n'
        f'Твой id: {message.from_user.id}\n\n'
        f'Этот tg_bot, домашняя работа для Университета Искусственного Интелекта, лекция №15.\n\n'
        f'Тема: Бот помогает выбрать напитки и еду из предложенного ассортимента, уточняет адрес и время доставки.\n\n'        
        f'Для перехода к тестированию нужно написать \n(! или кликнуть  ) команду \n\n/menu'        
        )


# выбор раздела (заказ еды или что то другое)
@dp.message_handler(Command("menu"))
async def menu(message: types.Message):
    await message.answer('Привет, желаешь сделать заказ еды?', reply_markup=first_kb)
    

# вывод меню (Пицца, Паста, напитки....)
@dp.message_handler(text='Да конечно!')
async def menu_select(message: types.Message, state: FSMContext):   
    await message.answer('Все кухни мира к твоим услугам!', reply_markup=main_kb)

    # открыл на запись test1 = State()
    await MenuFsm.test1.set()


# вывод меню Мясная, Рыбная, Фруктовая.. !команда цитирование!
@dp.message_handler(text=('Пицца'), state=MenuFsm.test1)
async def menu_select1(message: types.Message, state: FSMContext):    
    await message.reply(f'{message.from_user.full_name}, !здесь я применил цитирование!\n\nТеперь перейдем к начинкам', reply_markup=pizza_kb_kind)

    # записал test1 = State()
    answer = message.text
    await state.update_data(test1=answer)
    
    # контр. распечатка в терминал
    data = await state.get_data()
    step1 = data.get('test1') # ЗДЕССЬ ТОЛЬКО ЗАПИСАЛСЯ И ВЫВЕЛСЯ TEST1      
    # print(f'state1: {step1}\n')

     # открыл на запись test2 = State() (мясная или из рыбная, фрктовая)
    await MenuFsm.test2.set()


# переключает на выбор  мясных начинок для пиццы
@dp.message_handler(text=('Мясная'), state=MenuFsm.test2)
async def taste_pizza(message: types.Message, state: FSMContext):
    await message.answer('Пока все это работает, переходим к начинкам:', reply_markup=pizza_kb_meat_staffing)

    # записал test2 = State()
    answer = message.text
    await state.update_data(test2=answer)    

     # открыл на запись test3 = State() (начинка)
    await MenuFsm.test3.set()


# переключает на выбор  рыбных начинок для пиццы
@dp.message_handler(text=('Рыбная'), state=MenuFsm.test2)
async def taste_pizza(message: types.Message, state: FSMContext):
    await message.answer('Пока все это работает, переходим к начинкам:', reply_markup=pizza_kb_fish_staffing)

    # записал test2 = State()
    answer = message.text
    await state.update_data(test2=answer)

     # открыл на запись test3 = State() (начинка)
    await MenuFsm.test3.set()


# переключает на выбор  фруктовых начинок для пиццы
@dp.message_handler(text=('Фруктовая'), state=MenuFsm.test2)
async def taste_pizza(message: types.Message, state: FSMContext):
    await message.answer('Пока все это работает, переходим к начинкам:', reply_markup=pizza_kb_fruit_staffing)
    
    # записал test2 = State()
    answer = message.text
    await state.update_data(test2=answer)

     # открыл на запись test3 = State() (начинка)
    await MenuFsm.test3.set()


# после выбора начинки перекдючает на выбор размера
dict_staffing = ['Сырная с ветчиной', 'Пепперони по-деревенски', 'Пепперони', 'Пепперони по-деревенски', 'Ветчина и грибы', 'Чикен BBQ', 'Диабло', 'Лосось 🦈', 'Креветки 🦐', 'Мидии 🐙', 'Морские твари 🦑', 'Ананас', 'Апельсин', 'Манго', 'Фруктовое ассорти']

@dp.message_handler(Text(equals=dict_staffing, ignore_case=True), state=MenuFsm.test3)
async def size_pizza(message: types.Message, state: FSMContext):
    await message.answer('Отлично, теперь выбери размерчик пиццы:', reply_markup=pizza_kb_size)

    # записал test3 = State()
    answer = message.text
    await state.update_data(test3=answer)

    # открыл на запись test4 = State() (размер пиццы)
    await MenuFsm.test4.set()

   
# после выбора размера переключает на выбор напитка
dict_size = ['Большая 50 см. (900 гр.)', 'Средняя 30 см. (600 гр.)']

@dp.message_handler(Text(equals=dict_size, ignore_case=True), state=MenuFsm.test4)
async def drinks_menu(message: types.Message, state: FSMContext):
    await message.reply('Отлично, что из напитков?', reply_markup=drink_kb)

    # записал test4 = State()
    answer = message.text
    await state.update_data(test4=answer)

    # открыл на запись test5 = State() (размер пиццы)
    await MenuFsm.test5.set()


# после выбора напитка, записываю и закрываю запись
dict_drinks = ["Pepsi 0.5", "7UP 0.5", "Pepsi Max 0.5", "Aqua Minerale 0.5", "Lipton 0.5", "Adrenaline Rush 0.25"]

@dp.message_handler(Text(equals=dict_drinks, ignore_case=True), state=MenuFsm.test5)
async def drinks_menu(message: types.Message, state: FSMContext):

    # записал test5 = State()
    answer = message.text
    await state.update_data(test5=answer)
            
    # Вывод итоговой инфы клиенту    
    data = await state.get_data()
    step1 = data.get('test1') 
    step2 = data.get('test2') 
    step3 = data.get('test3') 
    step4 = data.get('test4') 
    step5 = data.get('test5') 

    await message.answer(            
        f'{message.from_user.full_name}, твой выбор:\n'
        f'{step1}\n'
        f'{step2}\n'
        f'{step3}\n'
        f'{step4}\n'
        f'{step5}\n'
        f'\nВсе верно?\n', reply_markup=yes_or_no_kb
    )

    # закрытие записи state
    await state.finish()
