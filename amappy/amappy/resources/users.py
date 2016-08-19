#! /usr/bin/env python
# endcoding: utf8

"""Users resources
"""

USERS = []


def get_users(id=None, name=None):
    return USERS


def create_user(data=None):
    from datetime import datetime
    from uuid import uuid4

    identifier = str(uuid4().hex)
    print identifier
    user = {
        "id":            identifier,
        "name":          data.get("name", ""),
        "first_name":    data.get("first_name", ""),
        "creation_date": data.get("creation_date", datetime.utcnow()),
        "email":         data.get("email", ""),
    }

    USERS.append(user)
    return identifier


def delete_user(id=None, name=None):
    pass


def update_user(id=None, name=None, data=None):
    pass
