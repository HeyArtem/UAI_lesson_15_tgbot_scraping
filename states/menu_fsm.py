from aiogram.dispatcher.filters.state import StatesGroup, State


'''
Здесь класс, который записывает состояния fsm
'''


class MenuFsm(StatesGroup):
    #  Пицца, паста, Пельмени, Напитки
    test1 = State()

    # Вид пиццы (мясная, рыбная...)
    test2 = State()

    # Начинка пиццы (лосось, салями, манго ...)
    test3 = State()
    
    # рвзмер пиццы
    test4 = State()

    # напиток
    test5 = State()    
