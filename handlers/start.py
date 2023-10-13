from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import start_keyboard


async def start_button(message: types.Message):
    print(message)
    Database().sql_insert_user_query(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Hello im you first bot',
        reply_markup=await start_keyboard()
    )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])