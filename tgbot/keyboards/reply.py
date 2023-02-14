from aiogram.types import ReplyKeyboardMarkup

from tgbot.buttons.reply import START_GAME

USER_KEYBOARDS = ReplyKeyboardMarkup([
    [START_GAME]
], resize_keyboard=True)
