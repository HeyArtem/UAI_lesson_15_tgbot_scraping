from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

'''
Вся обычнай клавиатура (не илайн) используемая в проекте, кроме ветки с заказом еды
'''

# клавиатура
kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/menu') 
        ]
    ],
    
    resize_keyboard=True  # Что бы кнопки не были на пол экрана
)
