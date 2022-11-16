from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

'''
Инлайн Клавиатура задействованая в ветке с едой       
'''


# инлайн клавиатура ВКУСЫ пасты
pasta_inkb_kind=InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='С мясной начинкой', callback_data='С мясной начинкой')            
        ],
        [
            InlineKeyboardButton(text='С рыбной начинкой', callback_data='С рыбной начинкой')
        ]
    ],
    resize_keyboard=True
)


# инлайн клавиатура мясных НАЧИНОК пасты
pasta_inkb_staff_meat=InlineKeyboardMarkup(row_width=2,
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Тальятелле с куриной грудкой', callback_data='Тальятелле с куриной грудкой'),
            InlineKeyboardButton(text='Карбонара', callback_data='Карбонара')            
        ],
    ],
    resize_keyboard=True
)


# инлайн клавиатура рыбных НАЧИНОК пасты
pasta_inkb_staff_fish=InlineKeyboardMarkup(row_width=2,
    inline_keyboard = [
        [
            InlineKeyboardButton(text='C лососем', callback_data='C лососем')            
        ],
        [
            InlineKeyboardButton(text='С креветками', callback_data='С креветками')
        ]
    ],
    resize_keyboard=True
)


# инлайн клавиатура напитков  (т.к. ве меню пасты я реализую на Инлайн кнопках)
pasta_inkb_drinks=InlineKeyboardMarkup(row_width=2,
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Pepsi 0.5', callback_data='Pepsi 0.5'),
            InlineKeyboardButton(text='7UP 0.5', callback_data='7UP 0.5'),
        ],
        [
            InlineKeyboardButton(text='Aqua Minerale 0.5', callback_data='Aqua Minerale 0.5'),
            InlineKeyboardButton(text='Adrenaline Rush 0.25', callback_data='Adrenaline Rush 0.25'),
        ]
    ],
    resize_keyboard=True
)


# инлайн коавиатура ДА или НЕТ
yes_or_no_kb = InlineKeyboardMarkup(row_width=2, 
inline_keyboard=[
    [
        InlineKeyboardButton(text='Да', callback_data='yes'),
        InlineKeyboardButton(text='Нет', callback_data='no'),
    ]
])
