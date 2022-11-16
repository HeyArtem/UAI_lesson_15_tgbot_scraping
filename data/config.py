import os
from dotenv import load_dotenv



load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

# это админы бота
admins = [
    564764469
]
