#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Users resources
"""

from amappy.persistence import UsersDB


def extract_id_or_name(id_or_name):
    try:
        id, name = int(id_or_name), None
    except ValueError:
        id, name = None, id_or_name
    except TypeError:
        id, name = None, None
    return id, name


def get_user(id_or_name=None):
    id, name = extract_id_or_name(id_or_name)
    return UsersDB.read(id=id, name=name)


def get_users():
    return UsersDB.read()


def create_user(data=None):
    return UsersDB.create(data=data)


def delete_user(id_or_name=None):
    id, name = extract_id_or_name(id_or_name)
    return UsersDB.delete(id=id, name=name)


def update_user(id_or_name=None, data=None):
    id, name = extract_id_or_name(id_or_name)
    return UsersDB.update(id=id, name=name, data=data)
