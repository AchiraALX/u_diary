#!/usr/bin/env python3
"""The Database storage"""

from base_model import Base
from sqlalchemy.orm import (
    sessionmaker
)
from sqlalchemy import create_engine

class DBStroge:
    """DB Engine"""
    engine = None
    session = sessionmaker()

    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://diary:diarydb@localhost/diary"
        )


db = DBStroge()
