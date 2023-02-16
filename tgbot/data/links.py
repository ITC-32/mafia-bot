def get_room_link(room_id: int, room_owner_id: int, bot_username: str):
    return f'https://t.me/{bot_username}?start=room_{room_owner_id}_{room_id}'
