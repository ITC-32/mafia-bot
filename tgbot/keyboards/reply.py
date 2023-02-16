from aiogram.types import ReplyKeyboardMarkup

from tgbot.buttons.reply import CREATE_ROOM, OWNER_ENTER_ROOM, START_GAME

USER_KEYBOARDS = ReplyKeyboardMarkup([
    [CREATE_ROOM]
], resize_keyboard=True)

OWNER_ENTER_ROOM_KEYBOARD = ReplyKeyboardMarkup([
    [OWNER_ENTER_ROOM]
], resize_keyboard=True)

START_GAME_KEYBOARD = ReplyKeyboardMarkup([
    [START_GAME]
], resize_keyboard=True)
