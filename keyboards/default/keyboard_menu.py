from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


'''
Все Клавиатуры (обычные, не инлайн) используемые в ветке с заказом еды
-с ассортиментом еды, 
-со вкусами пиццы, 
-с размером пиццы
-напитками
'''

# выбор разделов (заказ еды или что то другое)
first_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Да конечно!')
        ],
        [
            KeyboardButton(text='Нет, тот раздел меня уже не интересует!')
        ]
    ],
    resize_keyboard=True
)


# клава выбора с разделами еды () Пицца, Пельмени, Напитки и др
main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Пицца'),
            KeyboardButton(text='Паста (inline_kb)')
        ],
        [
            # KeyboardButton(text='Пельмени'),
            # KeyboardButton(text='Напитки'),
        ],     
    ],
    resize_keyboard=True
)


# клавиатура ВКУСЫ пиццы
pizza_kb_kind=ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Мясная'),
            KeyboardButton(text='Рыбная')
        ],
        [
            KeyboardButton(text='Фруктовая')
        ],
        [
            # KeyboardButton(text='↩️ Назад в основное меню')
        ]
    ],
    resize_keyboard=True
)


# клавиатура НАЧИНКИ мясной пиццы
pizza_kb_meat_staffing = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сырная с ветчиной'),
            KeyboardButton(text='Пепперони по-деревенски')
        ],
        [
            KeyboardButton(text='Пепперони'),
            KeyboardButton(text='Ветчина и грибы')
        ],
        [
            KeyboardButton(text='Чикен BBQ'),
            KeyboardButton(text='Диабло')
        ],
        [
            # KeyboardButton(text='↩️ Назад в основное меню')
        ]
    ],
    resize_keyboard=True
)


# клавиатура НАЧИНКИ рыбной пиццы
pizza_kb_fish_staffing = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Лосось 🦈'),
            KeyboardButton(text='Креветки 🦐')
        ],
        [
            KeyboardButton(text='Мидии 🐙'),
            KeyboardButton(text='Морские твари 🦑')
        ],        
        [
            # KeyboardButton(text='↩️ Назад в основное меню')
        ]
    ],
    resize_keyboard=True
)


# клавиатура НАЧИНКИ фруктовой пиццы
pizza_kb_fruit_staffing = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ананас'),
            KeyboardButton(text='Апельсин')
        ],
        [
            KeyboardButton(text='Манго'),
            KeyboardButton(text='Фруктовое ассорти')
        ],        
        [
            # KeyboardButton(text='↩️ Назад в основное меню')
        ]
    ],
    resize_keyboard=True
)


# клавиатура Размер пиццы
pizza_kb_size=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Большая 50 см. (900 гр.)'),
            KeyboardButton(text='Средняя 30 см. (600 гр.)')
        ],
        [
            # KeyboardButton(text='↩️ Назад в основное меню')
        ]        
    ],
    resize_keyboard=True
)


# клавиатура с напитками
drink_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi 0.5"),
            KeyboardButton(text="7UP 0.5"),
            KeyboardButton(text="Pepsi Max 0.5")
        ],
        [
            KeyboardButton(text="Aqua Minerale 0.5"),
            KeyboardButton(text="Lipton 0.5"),
            KeyboardButton(text="Adrenaline Rush 0.25"),
        ]
    ],
    resize_keyboard=True
)

