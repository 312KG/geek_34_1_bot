from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
GROUP_ID = [-1001663908187, ]
DESTINATION = "D:/PycharmProjects/pythonProject/geek_34_1_bot/media"