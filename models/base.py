#!/usr/bin/env python3
"""Define the base class
"""

from sqlalchemy import (
    DateTime
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)
from datetime import datetime


class Base(DeclarativeBase):
    """This class will contain common attributes"""
    id: Mapped[int] = mapped_column(
        nullable=False,
        primary_key=True
    )
    created_on: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    updated_on: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    def __repr__(self):
        return "<{} {}>"\
            .format(
                self.id,
                self.updated_on
            )

#
# Copyright (c) 2023
# Jacob A. Obara
# All rights reserved.
#
