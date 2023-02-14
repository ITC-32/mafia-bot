from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.commands.user import Commands
from tgbot.keyboards.reply import USER_KEYBOARDS
from tgbot.models.models import Users


async def user_start(message: Message):
    user = await Users.query.where(
        Users.tg_id == message.from_user.id
    ).gino.first()
    if not user:
        await Users.create(tg_id=message.from_user.id)
    await message.reply(
        'Привет! Это бот для игры в мафии',
        reply_markup=USER_KEYBOARDS
    )


async def new_game(message: Message):
    pass


def register_user(dp: Dispatcher):
    dp.register_message_handler(
        user_start, commands=['start'], state='*', commands_prefix='!/'
    )
    dp.register_message_handler(
        new_game, text=Commands.new_game.value
    )
