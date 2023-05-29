#!/usr/bin/env python3
"""Define the user class"""
from base_model import Base
from entries import Entries
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

class User(Base):
    """User class"""

    __tablename__ = "users"

    user_name: Mapped[str] = mapped_column(String(50))
    user_fullname: Mapped[str] = mapped_column(String(100))

    entries: Mapped[List["Entries"]] = relationship(back_populates="user_id")

    def __repr__(self) -> str:
        return (
            f"User(user_id={self.user_id!r}) -> \
            user_name={self.user_name!r}\
            user_fullname={self.user_fullname!r}"
        )
