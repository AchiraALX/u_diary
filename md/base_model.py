#!/usr/bin/env python3

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
    Session,
    relationship,
    Mapped,
    mapped_column
)
from datetime import datetime

class Base(DeclarativeBase):
    """This class will contain common attributes"""
    o_id: Mapped[str] = mapped_column(String(60), nullable=False, primary_key=True)
    c_on: Mapped[str] = mapped_column(DateTime, nullable=False, default=datetime.utcnow())
    u_on: Mapped[str] = mapped_column(DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return self.__str__()
