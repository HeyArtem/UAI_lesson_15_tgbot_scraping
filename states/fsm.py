from aiogram.dispatcher.filters.state import StatesGroup, State


'''
Сосотояния для Мини тест-опроса для FSM 

конечный автомат (finite-state machine, FSM) — 
это математическая абстракция, модель, которая может находиться только в одном 
из конечного числа состояний в каждый конкретный момент времени. 
Автомат умеет переходить из одного состояния в другое в ответ на данные, 
которые подаются на вход; 
изменение состояния называется переходом. 
FSM определяется списком его состояний, начальным состоянием и инпутами, запускающими переходы.
'''


class TestFsm(StatesGroup):

    # Твое имя?
    test1 = State()

    # Любимая модель авто
    test2 = State()

    # Любимая сторона света
    test3 = State()