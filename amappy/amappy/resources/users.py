#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Users resources
"""

from amappy.persistence import UsersDB


def get_user(id=None, name=None):
    return UsersDB.read(id=id, name=name)


def get_users():
    return UsersDB.read()


def create_user(data=None):
    return UsersDB.create(data)


def delete_user(id=None, name=None):
    UsersDB.delete(id=id, name=name)


def update_user(id=None, name=None, data=None):
    return UsersDB.update(id=id, name=name, data=data)
