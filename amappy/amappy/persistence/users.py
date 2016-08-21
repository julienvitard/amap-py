#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Users persistence
"""

from amappy.persistence.base import Persistence


class UsersMemoryDB(Persistence):
    USERS_BY_ID = {}
    USERS_BY_NAME = {}

    @classmethod
    def get_id(cls):
        ids = cls.USERS_BY_ID.values()
        return (ids and max(ids) + 1) or 1

    @classmethod
    def create(cls, data):
        from datetime import datetime
        if data["name"] in cls.USERS_BY_NAME.keys():
            raise ValueError("User already exists")

        identifier = cls.get_id()
        creation_date = datetime.utcnow()

        data["id"] = identifier
        data["creation_date"] = creation_date

        cls.USERS_BY_ID[identifier] = data
        cls.USERS_BY_NAME[data["name"]] = data

        return identifier

    @classmethod
    def read(cls, id=None, name=None):
        try:
            if id:
                return cls.USERS_BY_ID[id]
            elif name:
                return cls.USERS_BY_NAME[name]
        except KeyError:
            return None
        return list(cls.USERS_BY_ID.values())

    @classmethod
    def update(cls, id=None, name=None, data=None):
        user = None
        if id:
            user = cls.USERS_BY_ID[id]
            user.update(data)
        elif name:
            user = cls.USERS_BY_NAME[name]
            user.update(data)
        return user

    @classmethod
    def delete(cls, id=None, name=None):
        if id:
            user = cls.USERS_BY_ID[id]
            cls.USERS_BY_NAME.pop(user["name"])
            cls.USERS_BY_ID.pop(id)
            del user
        elif name:
            user = cls.USERS_BY_NAME[name]
            cls.USERS_BY_ID.pop(user["id"])
            cls.USERS_BY_NAME.pop(name)
            del user

    @classmethod
    def reset(cls):
        cls.USERS_BY_ID = {}
        cls.USERS_BY_NAME = {}


UsersDB = UsersMemoryDB
