from aiogram import Dispatcher

from tgbot.handlers.echo import register_echo
from tgbot.handlers.users import register_all_user_handlers


def register_all_handlers(dp: Dispatcher):
    register_all_user_handlers(dp)
    register_echo(dp)
