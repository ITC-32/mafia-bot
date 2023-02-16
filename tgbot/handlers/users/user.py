from aiogram import Dispatcher
from aiogram.types import Message
from sqlalchemy import and_
from sqlalchemy.sql.operators import is_

from tgbot.keyboards.reply import USER_KEYBOARDS
from tgbot.models.models import Users, Room, GameMembers


async def user_start(message: Message):
    user = await Users.query.where(
        Users.tg_id == message.from_user.id
    ).gino.first()
    if not user:
        await Users.create(tg_id=message.from_user.id)
    if 'room' in message.text:
        split_text = message.text.split('_')
        owner_id, room_id = int(split_text[-2]), int(split_text[-1])
        found_room: Room = await Room.query.where(and_(
            Room.Id == room_id,
            Room.owner == owner_id,
            is_(Room.active_status, True),
            is_(Room.busy, False)
        )).gino.first()
        if not found_room:
            await message.answer('Комната не найдена! Возможно игра уже завершилась')
            return
        current_member: GameMembers = await GameMembers.query.where(
            GameMembers.user_id == message.from_user.id
        ).gino.first()
        if current_member and current_member.is_playing:
            await message.answer('Вы уже находитесь в другом лобби')
            return
        if not current_member:
            await GameMembers.create(
                user_id=message.from_user.id, room_id=room_id
            )
        else:
            await current_member.update(is_playing=True).apply()
        username = message.from_user.username
        await message.bot.send_message(
            found_room.owner,
            f'В комнату присоединился участник! {f"Его ник: @{username}" if username else f"Его имя {message.from_user.full_name}"}'
        )
        await message.answer('Вы успешно вошли в игру! Ждём пока админ начнёт игру!')
    else:
        await message.reply(
            'Привет! Это бот для игры в мафии',
            reply_markup=USER_KEYBOARDS
        )


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_start, commands=['start'], state='*', commands_prefix='!/'
    )
