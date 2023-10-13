from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="poker_yes"
    )
    no_button = InlineKeyboardButton(
        "No",
        callback_data="poker_no"
    )
    markup.add(yes_button)
    markup.add(no_button)
    return markup