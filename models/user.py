#!/usr/bin/env python3
"""Define the user class"""
from models.base import Base
from models.entries import Entry, EntryComment
from sqlalchemy import String
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship
)
from typing import List


class User(Base):
    """User class"""

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Relationships
    entries = relationship(
        Entry,
        back_populates="author_info"
    )
    comments = relationship(
        EntryComment,
        back_populates='author_info'
    )

    def __repr__(self) -> str:
        return (
            "<User {}> id={} name={}"
            .format(
                self.username,
                self.id,
                self.name
            )
        )

#
# Copyright (c) 2023
# Jacob A. Obara
# All rights Reserved
#