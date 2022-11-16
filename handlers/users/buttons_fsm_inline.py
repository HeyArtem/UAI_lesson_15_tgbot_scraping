from aiogram import types
from loader import dp
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from states import MenuFsm
from keyboards.inline import (pasta_inkb_drinks, pasta_inkb_kind,
                              pasta_inkb_staff_fish, 
                              pasta_inkb_staff_meat,
                              yes_or_no_kb
                              )
from keyboards.default.keyboard_menu import first_kb


'''
Раздел Паста, весь на онлайн клаве
здесь все callback_query_handler
'''


# переключает на режим выбора вкусов для пасты 
@dp.message_handler(text='Паста (inline_kb)', state=MenuFsm.test1)
async def pasta_kind(message: types.Message, state: FSMContext):
    await message.answer('Раздел по пасте я реализовал на inline-keyboard\nКакой предпочитаете вкус?\n', reply_markup=pasta_inkb_kind)

    # записал test1 = State()
    answer = message.text
    await state.update_data(test1=answer)
    
    # контр. распечатка в терминал
    data = await state.get_data()
    step1 = data.get('test1') # ЗДЕССЬ ТОЛЬКО ЗАПИСАЛСЯ И ВЫВЕЛСЯ TEST1      
    # print(f'state1: {step1}\n')

    # открыл на запись test2 = State() (мясная или из рыбная, фрктовая)
    await MenuFsm.test2.set()


# переключает на выбор мясных начинок для пасты  !Инлайн клава! types.CallbackQuery
@dp.callback_query_handler(text='С мясной начинкой', state=MenuFsm.test2)
async def pasta_meat(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Какой вкус больше нравится?\n', reply_markup=pasta_inkb_staff_meat)
   
    # записал test2 = State()  #  в callback_query_handler реакцию доставать из call.data    
    answer = call.data    
    await state.update_data(test2=answer)
    
    # контр. распечатка в терминал
    data = await state.get_data()
    step1 = data.get('test1') 
    step2 = data.get('test2') 
    # print(
    #     f'state1: {step1}\n'
    #     f'state2: {step2}\n'
    #     )

     # открыл на запись test3 = State() (начинка)
    await MenuFsm.test3.set()
    await call.answer() #убирает часики на онлайн кнопке


# переключает на выбор рыбных начинок для пасты  !Инлайн клава!
@dp.callback_query_handler(text='С рыбной начинкой', state=MenuFsm.test2)
async def pasta_fish(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Какой вкус больше нравится?\n', reply_markup=pasta_inkb_staff_fish)

    # записал test2 = State()
    answer = call.data
    await state.update_data(test2=answer)

     # открыл на запись test3 = State() (начинка)
    await MenuFsm.test3.set()
    await call.answer() #убирает часики на онлайн кнопке


# после выбора начинки пасты переключает на выбор напитков  !Инлайн клава!
dict_staff_meat = ['Тальятелле с куриной грудкой', 'Карбонара', 'С креветками', 'C лососем'] 

@dp.callback_query_handler(Text(equals=dict_staff_meat, ignore_case=True), state=MenuFsm.test3)
async def pasta_drinks1(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Пока все это работает!!! \nПозвольте предложить напиток:', reply_markup=pasta_inkb_drinks)

    # записал test3 = State()
    answer = call.data    
    await state.update_data(test3=answer)

    # открыл на запись test4 = State() (начинка)
    await MenuFsm.test4.set()
    await call.answer() 


# после выбора напитка (ветка пасты) записываю последнее состояние и закрываю запись
dict_drinks = ["Pepsi 0.5", "7UP 0.5", "Pepsi Max 0.5", "Aqua Minerale 0.5", "Lipton 0.5", "Adrenaline Rush 0.25"]

@dp.callback_query_handler(Text(equals=dict_drinks, ignore_case=True), state=MenuFsm.test4)
async def pasta_total(call: CallbackQuery, state: FSMContext):

    # записал test4 = State()
    answer = call.data    
    await state.update_data(test4=answer)
    
    # вывод итоговой информации заказчику
    data = await state.get_data()
    step1 = data.get('test1') 
    step2 = data.get('test2') 
    step3 = data.get('test3') 
    step4 = data.get('test4')

    await call.message.answer(
        f'Итого весь заказ:\n'
        f'{step1}\n'
        f'{step2}\n'
        f'{step3}\n'
        f'{step4}\n'
        f'\n Все верно? \n', reply_markup=yes_or_no_kb
    ) 
    
    # закрытие записи
    await state.finish()
    await call.answer() #убирает часики на онлайн кнопке


# ловит Yes от инлайн клавы
@dp.callback_query_handler(text='yes')
async def total_yes(call: CallbackQuery):
    await call.message.answer('Поздравляю заказ оформлен!\n\nПротестим еще раз алгоритм заказа еды?', reply_markup=first_kb)
    await call.answer()


# ловит No от инлайн клавы
@dp.callback_query_handler(text='no')
async def total_yes(call: CallbackQuery):
    await call.message.answer('Заказ отменен\n\nДавай попробуем по новой!', reply_markup=first_kb)
    await call.answer() 
