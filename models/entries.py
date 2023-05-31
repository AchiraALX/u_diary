#!/usr/bin/env python3
"""Define the diary entries"""

from models.base import Base
from sqlalchemy import (
    ForeignKey,
    String
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship
)


class Entry(Base):

    __tablename__ = 'entries'

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    content: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    # Foreign key
    user: Mapped[str] = mapped_column(
        ForeignKey("users.username")
    )

    # Relationship
    author_info = relationship(
        'User',
        back_populates="entries"
    )
    comments = relationship(
        'EntryComment',
        back_populates='entry_info'
    )

    def __repr__(self) -> str:
        return (
            "<Entry {}> title={} body={} author={} comments={}"
            .format(
                self.id,
                self.title,
                self.content,
                self.author_info,
                self.comments
            )
        )


# Declare entry comment class
class EntryComment(Base):

    __tablename__ = 'entry_comments'

    comment: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    # Foreign key
    entry: Mapped[int] = mapped_column(
        ForeignKey("entries.id")
    )
    author: Mapped[str] = mapped_column(
        ForeignKey("users.username")
    )

    # Relationship
    entry_info = relationship(
        'Entry',
        back_populates="comments"
    )
    author_info = relationship(
        'User',
        back_populates="comments"
    )

    def __repr__(self) -> str:
        return (
            "<EntryComment {}> comment={} entry={}"
            .format(
                self.id,
                self.comment,
                self.entry_info,
                self.author_info
            )
        )

#
# Copyright (c) 2023
# Jacob A. Obara
# All rights reserved.
#
