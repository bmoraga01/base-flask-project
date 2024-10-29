from ..db import db, BaseModelMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, ForeignKey, Boolean
from datetime import date
from typing import List

class Band(db.Model, BaseModelMixin):
    __tablename__ = 'band'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(length=150), unique=True, nullable=False)
    origin: Mapped[str] = mapped_column(String(length=250), nullable=False)
    state: Mapped[bool] = mapped_column(Boolean(), default=True)
    gender: Mapped[str] = mapped_column(String(length=150), nullable=False)
    founded: Mapped[date] = mapped_column(Date(), nullable=False)
    members: Mapped["List[Member]"] = relationship()
    
    def __int__(self, name: str, origin: str, state: bool, gender: str, founded: date):
        self.name = name
        self.origin = origin
        self.state = state
        self.gender = gender
        self.founded = founded
        
    def __repr__(self) -> str:
        return f'<Band {self.name}>'
    
    def __str__(self) -> str:
        return f'Band {self.name}'
    
class Member(db.Model, BaseModelMixin):
    __tablename__ = 'member'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(length=200), nullable=False)
    nickname: Mapped[str] = mapped_column(String(length=150), nullable=False)
    birthdate: Mapped[date] = mapped_column(Date(), nullable=False)
    instruments: Mapped[str] = mapped_column(String(length=200), nullable=False)
    id_band: Mapped[int] = mapped_column(ForeignKey('band.id'), nullable=False)
    
    def __init__(self, name: str, nickname: str, birthdate: date, instruments: str, id_band: int) -> None:
        self.name = name
        self.nickname = nickname
        self.birthdate = birthdate
        self.instruments = instruments
        self.id_band = id_band
        
    def __repr__(self) -> str:
        return f'<Member {self.name}>'
    
    def __str__(self) -> str:
        return f'Member {self.name}'