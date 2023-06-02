#!/usr/bin/env python3
"""Query script
"""

from models.entries import (
    Entry,
    EntryComment
)
from models.user import User
from storage import Storage
from graphene import (
    ObjectType,
    DateTime,
    String,
    Int,
    Schema,
    List
)
import json


# UserType
class UserType(ObjectType):
    """UserType class

    Args:
        ObjectType (Inherited): graphene ObjectType
    """
    id = Int()
    created_on = DateTime()
    Updated_on = DateTime()
    username = String()
    name = String()
    entries = List(lambda: EntryType)
    comments = List(lambda: EntryCommentType)


# Declare EntryType
class EntryType(ObjectType):
    """EntryType class

    Args:
        ObjectType (_type_): Graphene ObjectType
    """
    id = Int()
    created_on = DateTime()
    updated_on = DateTime()
    title = String()
    content = String()
    user = String()


# Declare EntryCommentType
class EntryCommentType(ObjectType):
    """EntryCommentType class

    Args:
        ObjectType (class): Graphene ObjectType
    """
    id = Int()
    created_on = DateTime()
    updated_on = DateTime()
    comment = String()
    entry = Int()
    author = String()


# Declare query class
class Query(ObjectType):
    """Definition for resolvers

    Args:
        ObjectType (class): Graphene ObjectType
    """

    users = List(UserType)
    entries = List(EntryType)
    comments = List(EntryCommentType)

    def resolve_users(self, info):
        """Resolve for users

        Args:
            info (object): GraphQL Object
        """
        users = Storage().new().query(User).all()
        entries = Storage().new().query(Entry).all()
        comments = Storage().new().query(EntryComment).all()

        users_list = [user.__dict__ for user in users]
        for user in users_list:
            user['entries'] = [
                entry.__dict__ for entry in
                entries if entry.user == user['username']
            ]
            user[
                'comments'
            ] = [
                comment.__dict__ for comment in
                comments if comment.author == user[
                    'username'
                ]
            ]

        return users_list

    def resolve_entries(self, info):
        """Query resolving the entries

        Args:
            info (object): GraphQL Object
        """
        entries = Storage().new().query(Entry).all()

        entry_list = [entry.__dict__ for entry in entries]

        return entry_list

    def resolve_comments(self, info):
        """Query resolving the comments

        Args:
            info (object): GraphQL Object
        """

        comments = Storage().new().query(EntryComment).all()

        comment_list = [comment.__dict__ for comment in comments]

        return comment_list

    def __repr__(self):
        return (
            "Query class for resolving objects"
        )



def execute_query(query):
    schema = Schema(query=Query)
    result = schema.execute(query)
    if result.errors:
        print(result.errors)
    else:
        return dict(result.data.items())


def main(query: str = None) -> dict:
    """Main query
    """
    if query is None:
        return {
            'error': "Query not specified."
        }

    users = '''
    {
        users {
            id
            username
            name
            entries {
                id
                title
                content
                user
            }
            comments {
                id
                comment
                entry
                author
            }
        }
    }
    '''
    entries = '''
    {
        entries {
            id
            title
            content
            user
        }
    }
    '''
    comments = '''
    {
        comments {
            id
            comment
            entry
            author
        }
    }
    '''

    queries = {
        'users': users,
        'entries': entries,
        'comments': comments
    }

    for key, value in queries.items():
        if key == query:
            data = {
                **execute_query(value)
            }

    return data


if __name__ == "__main__":
    data = main('entries')
    print(data)