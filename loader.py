from aiogram import Bot, Dispatcher, types
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# пременная бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# хранилище оперативной памяти
storage = MemoryStorage()

# # диспетчер
# dp = Dispatcher(bot)

# при работе с FSM мне нужен будет пользоваться памятью для записи состояний
dp = Dispatcher(bot, storage=storage)
