#!/usr/bin/env python3
"""The Database storage"""

from models.base import Base
from models.user import User
from models.entries import (
    Entry,
    EntryComment
)
from sqlalchemy.orm import (
    Session
)
from sqlalchemy import create_engine


class Storage:
    """DB Engine"""

    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://diary:diarydb@localhost/diary"
        )

        # Create all tables in the engine
        Base.metadata.create_all(self.engine)

        # Bind the engine to the metadata of the Base class
        self.session = Session(bind=self.engine)

    # Create new session
    def new(self):
        """Create new session"""
        return self.session

    # Commit all changes of the current session
    def save(self, obj):
        """Commit all changes of the current session"""
        ses = self.new()
        ses.add(obj)
        ses.flush()
        ses.commit()

    # Rollback incase of error or early quit
    def rollback(self):
        """Rollback incase of error or early quit"""
        ses = self.new()
        ses.rollback()

    # Close the current session
    def close(self):
        """Close the current session"""
        self.session.close()

    # Storage representation
    def __repr__(self):
        """A string representation of the database
        """
        ses = self.new()
        if ses.new:
            return (
                "<Uncommitted changes{}>"
                    .format(ses.new)
            )

        elif self.engine:
            return "<<Connected with no uncommitted changes.>"

        else:
            return "<<Unconnected to any database.>"


if __name__ == "__main__":
    storage = Storage()
    print(storage.__repr__())


#
# Copyright (c) 2023
# Jacob A. Obara
#
