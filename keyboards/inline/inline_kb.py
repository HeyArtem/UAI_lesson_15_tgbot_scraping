from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

'''
Вся инлайн клавиатура, кроме используемой в ветке с едой   
'''


# инлайн клавиатура после 'Нет этот раздел меня больше не интересует'
ikb_no_eat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Образование по Python', url='https://neural-university.ru/'),
            InlineKeyboardButton(text='GitHub Артёма', url='https://github.com/HeyArtem'),
        ],
        [
            InlineKeyboardButton(text='👨🏼‍💻 Заглушка', callback_data='Заглушка'),
            InlineKeyboardButton(text='Мини FSM', callback_data='fsmt'),
        ],
        [
            InlineKeyboardButton(text='Dixy (парсинг)', callback_data='Scraping')
        ],
        [
            InlineKeyboardButton(text='↩️  Назад в основное меню', callback_data='menu')
        ],
    ],
    resize_keyboard=True
    )
