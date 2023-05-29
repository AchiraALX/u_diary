#!/usr/bin/env python3
"""Define the diary entries"""
from user import User
from base_model import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)

class Entries(Base):

    __tablename__ = 'entries'
    
    entry_title: Mapped[str]
    entry_body: Mapped[str]
    entry_user = mapped_column(ForeignKey("users.user_id"))

    user_id: Mapped[User] = relationship(back_populates="entries")

    def __repr__(self) -> str:
        return (
            f"Entry(id={self.entry_id!r} -> \
            entry_title={self.entry_title!r}) \
            entry_body={self.entry_body!r}"
        )

