from decouple import config
from aiogram import Bot, Dispatcher

TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
