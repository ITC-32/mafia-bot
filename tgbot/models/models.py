from gino import Gino
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

db = Gino()


class Users(db.Model):

    __tablename__ = 'users'

    tg_id = Column(Integer(), primary_key=True)


class Room(db.Model):

    __tablename__ = 'room'

    Id = Column(Integer(), primary_key=True)
    name = Column(String(120))
    owner = Column(ForeignKey("users.tg_id"))
    active_status = Column(Boolean, default=True)
    busy = Column(Boolean, default=False)


class GameMembers(db.Model):

    __tablename__ = 'game_members'

    Id = Column(Integer(), primary_key=True)
    user_id = Column(ForeignKey("users.tg_id"))
    room_id = Column(ForeignKey("room.Id"))
    is_playing = Column(Boolean, default=True)
