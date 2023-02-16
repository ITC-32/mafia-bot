from aiogram.types import KeyboardButton

from tgbot.commands.user import Commands

CREATE_ROOM = KeyboardButton(Commands.new_game.value)
OWNER_ENTER_ROOM = KeyboardButton(Commands.owner_enter.value)
START_GAME = KeyboardButton(Commands.start_game.value)
