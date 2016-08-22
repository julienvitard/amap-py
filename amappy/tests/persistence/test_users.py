#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestUsersMemoryDB(unittest.TestCase):

    def test_users_memory_db_init(self):
        from amappy.persistence.users import UsersMemoryDB
        db = UsersMemoryDB
        self.assertEqual(db.USERS_BY_ID, {})
        self.assertEqual(db.USERS_BY_NAME, {})
