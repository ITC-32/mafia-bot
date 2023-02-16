from aiogram.dispatcher.filters.state import StatesGroup, State


class RoomOwnerEnterState(StatesGroup):
    activate_room = State()


class GameLoopState(StatesGroup):
    wait_start = State()
    imposters_ids = State()
