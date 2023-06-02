#!/usr/bin/env python3
"""Add data to DB"""

from storage import Storage
from models.user import User
from models.entries import (
    Entry,
    EntryComment
)

# Declare class Add
class Add:
    """Add data into the DB
    """

    db = Storage()
    failed = []

    def add_user(
        self,
        username: str = None,
        name: str = None
    ) -> User:
        """An instance for adding a user
        """
        details = {
            'username': username,
            'name': name,
        }

        obj = self.unpack_and_save(details, User)

        return obj


    def add_entry(
        self,
        title: str = None,
        content: str = None,
        author_info: User = None
    ) -> Entry:
        """An instance for adding an entry
        """
        details = {
            'title': title,
            'content': content,
            'author_info': author_info
        }

        obj = self.unpack_and_save(
            details=details,
            model=Entry
        )

        return obj

    def add_comment(
        self,
        comment: str = None,
        entry_info: Entry = None,
        author_info: User = None
    ) -> EntryComment:
        """An instance for adding an entry comment
        """
        details = {
            'comment': comment,
            'entry_info': entry_info,
            'author_info': author_info
        }

        obj = self.unpack_and_save(
            details=details,
            model=EntryComment,
            int_check=['entry_info']
        )

        return obj

    def retrieve_entry(self, id: int):
        """An instance to query an entry

        Args:
            id (int): _description_

        Returns:
            _type_: _description_
        """
        return self.db.new()\
            .query(Entry)\
                .filter_by(id=id)\
                    .first()

    def retrieve_user(self, username: str) -> User:
        """An instance to query a user

        Args:
            username (str): _description_

        Returns:
            User: _description_
        """
        return self.db.new()\
            .query(User)\
                .filter_by(username=username)\
                    .first()

    def unpack_and_save(
        self,
        details: dict = None,
        model=None,
        int_check: list = [],
    ):
        """Saves the given data to the database
        """
        self.failed = []
        if details is None:
            return {
                'error': "Dictionary empty."
            }

        for key, value in details.items():
            if value is None:
                value = self.ask_field(key)

            if self.check_validity(value):
                if key in int_check:
                    value = self.check_for_int(value, key)

                match key:
                    case 'author_info':
                        value = self.retrieve_user(value)

                    case 'entry_info':
                        value = self.retrieve_entry(value)

                details[key] = value

            else:
                self.failed.append(key)

        if len(self.failed) > 0:
            print(f"Some values failed {self.failed}")
            return

        details = model(**details)

        try:
            self.add_to_db(details)

        except Exception as e:
            print(e)

        return details


    def add_to_db(self, obj):
        """Instance fo saving data in the session

        Args:
            obj (_): obj to be saved
        """

        self.db.save(obj)

    def ask_field(self, field: str) -> str:
        """Ask for input and return it

        Args:
            field (str): the field description

        Returns:
            str: user input
        """

        return input(f"Enter {field!r}: ").strip()

    def check_for_int(self, value, field: str) -> int:
        """An instance for checking for integer

        Args:
            value (_): value to be checked

        Returns:
            int: value
        """

        while True:
            try:
                int(value)
                break
            except ValueError:
                print(f'{field!r} must be an integer')
                value = self.ask_field(field=field)

        return value

    def check_validity(self, value: str) -> bool:
        """An instance to check if a value was entered

        Args:
            value (str): value to be checked

        Returns:
            bool: True if a value exist else False
        """

        try:
            value = str(value)

        except Exception as e:
            print("Only strings are checked.")

        value = value.split(' ')

        if len(value) > 1:
            return True

        elif len(value) == 1 and len(value[0]) > 0:
            return True

        else:
            return False

    def __repr__(self) -> str:
        return (
            "Class for adding data into the database"
        )

if __name__ == "__main__":
    db = Add()
    print(db.add_entry())